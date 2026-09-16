#!/usr/bin/env python3
"""Generate the greybox ISA wireframes.

Greybox = labeled boxes only. No brand colour, no typography work, no imagery.
Every page names the wave-2 module that backs it in the footer.

Run: python3 gen_wireframes.py   (writes *.html next to this file)
"""
import html
import os

OUT = os.path.dirname(os.path.abspath(__file__))

MODULES = {
    "matching": "matching",
    "contracts": "contracts",
    "ledger": "ledger",
    "verification": "verification",
    "reporting": "reporting",
}

CSS = """
* { box-sizing: border-box; }
body { font: 13px/1.45 ui-monospace, Menlo, Consolas, monospace;
       background: #efefef; color: #222; margin: 0; padding: 24px; }
.page { max-width: 960px; margin: 0 auto; }
.crumb { font-size: 11px; color: #666; margin-bottom: 8px; }
.crumb a { color: #666; }
h1 { font-size: 18px; margin: 0 0 4px; }
.q { font-size: 12px; color: #555; margin: 0 0 20px; font-style: normal; }
.box { border: 1px dashed #999; background: #e2e2e2; padding: 10px 12px;
       margin: 0 0 14px; }
.box > .lbl { font-size: 10px; letter-spacing: .08em; text-transform: uppercase;
       color: #555; margin-bottom: 8px; }
.field { border: 1px solid #aaa; background: #f6f6f6; padding: 6px 8px;
       margin: 0 0 6px; font-size: 12px; }
.field .t { color: #777; font-size: 10px; float: right; }
.btn { display: inline-block; border: 1px solid #555; background: #ccc;
       padding: 5px 12px; margin: 4px 6px 0 0; font-size: 12px; }
.btn.secondary { background: #e8e8e8; border-style: dotted; }
table { width: 100%; border-collapse: collapse; background: #f6f6f6;
       font-size: 12px; }
th, td { border: 1px solid #aaa; padding: 5px 7px; text-align: left; }
th { background: #dcdcdc; font-weight: normal; font-size: 11px; }
td.stub { color: #888; }
ul.items { margin: 0; padding-left: 18px; }
ul.items li { margin: 0 0 4px; }
.note { border-left: 3px solid #999; padding: 6px 10px; margin: 0 0 14px;
       background: #e8e8e8; font-size: 12px; color: #444; }
.cols { display: flex; gap: 14px; }
.cols > * { flex: 1; }
.tiles { display: flex; gap: 10px; flex-wrap: wrap; }
.tile { border: 1px dashed #999; background: #e2e2e2; padding: 10px;
       min-width: 150px; flex: 1; }
.tile .k { font-size: 10px; text-transform: uppercase; color: #555; }
.tile .v { font-size: 20px; color: #666; }
footer { border-top: 1px solid #aaa; margin-top: 26px; padding-top: 10px;
       font-size: 11px; color: #555; }
footer b { font-weight: normal; background: #dcdcdc; padding: 1px 5px;
       border: 1px solid #aaa; }
"""


# ---------- block helpers -------------------------------------------------
def esc(s):
    return html.escape(str(s))


def form(legend, fields):
    rows = "".join(
        '<div class="field">%s<span class="t">%s</span></div>'
        % (esc(label), esc(kind))
        for label, kind in fields
    )
    return '<div class="box"><div class="lbl">Form — %s</div>%s</div>' % (
        esc(legend),
        rows,
    )


def actions(*labels):
    btns = "".join(
        '<span class="btn%s">%s</span>'
        % ("" if i == 0 else " secondary", esc(l))
        for i, l in enumerate(labels)
    )
    return '<div class="box"><div class="lbl">Actions</div>%s</div>' % btns


def table(caption, columns, rows=3):
    head = "".join("<th>%s</th>" % esc(c) for c in columns)
    body = "".join(
        "<tr>%s</tr>"
        % "".join('<td class="stub">%s row %d</td>' % (esc(c), r + 1)
                  for c in columns)
        for r in range(rows)
    )
    return (
        '<div class="box"><div class="lbl">Data region — %s</div>'
        "<table><tr>%s</tr>%s</table></div>" % (esc(caption), head, body)
    )


def region(label, items):
    lis = "".join("<li>%s</li>" % esc(i) for i in items)
    return (
        '<div class="box"><div class="lbl">Data region — %s</div>'
        '<ul class="items">%s</ul></div>' % (esc(label), lis)
    )


def tiles(label, pairs):
    ts = "".join(
        '<div class="tile"><div class="k">%s</div><div class="v">%s</div></div>'
        % (esc(k), esc(v))
        for k, v in pairs
    )
    return (
        '<div class="box"><div class="lbl">Status tiles — %s</div>'
        '<div class="tiles">%s</div></div>' % (esc(label), ts)
    )


def note(text):
    return '<div class="note">%s</div>' % esc(text)


def cols(*blocks):
    return '<div class="cols">%s</div>' % "".join(
        "<div>%s</div>" % b for b in blocks
    )


# ---------- the pages -----------------------------------------------------
PAGES = []


def page(slug, flow, title, question, modules, blocks):
    PAGES.append(
        dict(slug=slug, flow=flow, title=title, question=question,
             modules=modules, blocks=blocks)
    )


# --- learner flow ---------------------------------------------------------
page(
    "learner-apply", "Learner", "Learner application",
    "Can this person enter a cohort, and on what terms?",
    ["matching", "verification"],
    [
        note("Step 1 of 4. Progress bar: Apply / Screen / Offer / Sign."),
        form("Identity", [
            ("Full legal name", "text"),
            ("Email", "email"),
            ("Country of residence", "select"),
            ("Date of birth", "date"),
            ("Government ID upload", "file"),
        ]),
        form("Programme choice", [
            ("Provider", "select — from provider registry"),
            ("Cohort", "select — filtered by provider + open seats"),
            ("Start date preference", "select"),
            ("Study mode (full-time / part-time)", "radio"),
        ]),
        form("Income and eligibility", [
            ("Current employment status", "select"),
            ("Current gross annual income", "currency"),
            ("Highest qualification", "select"),
            ("Prior income evidence upload", "file — payslip or tax record"),
            ("Right-to-work status", "select"),
        ]),
        form("Consents", [
            ("Consent to income verification for the ISA term", "checkbox"),
            ("Consent to employer outcome reporting", "checkbox"),
            ("Consent to data processing notice", "checkbox — links notice"),
        ]),
        actions("Submit application", "Save draft", "Withdraw application"),
        region("Inline validation region", [
            "Field-level errors (blocking)",
            "Eligibility warning: income floor not met for this cohort",
            "Duplicate-application notice",
        ]),
    ],
)

page(
    "learner-status", "Learner", "Learner application status",
    "Where is my application, and what does it need from me?",
    ["matching", "verification"],
    [
        tiles("Application state", [
            ("Stage", "Screening"),
            ("Days in stage", "4"),
            ("Seat held until", "date"),
            ("Open tasks", "2"),
        ]),
        region("Timeline region — one row per state change", [
            "Submitted — date, actor",
            "Screened — date, actor, outcome",
            "Offer issued — date, expiry",
            "Agreement signed — date, contract id",
            "Enrolled — date, cohort id",
        ]),
        table("Outstanding tasks", ["Task", "Owner", "Due", "State"], 3),
        form("Document resubmission", [
            ("Document type", "select"),
            ("Replacement file", "file"),
            ("Note to reviewer", "textarea"),
        ]),
        actions("Upload document", "Message admissions", "Accept offer",
                "Decline offer"),
        note("Offer expiry countdown renders here when an offer is live."),
    ],
)

page(
    "learner-isa-terms", "Learner", "ISA terms and transparency view",
    "Exactly what will I pay, under which outcomes?",
    ["contracts", "ledger", "reporting"],
    [
        note("Transparency page. Pre-signature. Every number is sourced and "
             "dated; nothing here is marketing copy."),
        tiles("Headline terms", [
            ("Income share", "x% of gross"),
            ("Payment term", "n months"),
            ("Income floor", "currency / yr"),
            ("Payment cap", "multiple of tuition"),
        ]),
        region("Definitions region — plain-language, one per term", [
            "Gross income — what counts, what is excluded",
            "Income floor — no payment below this figure",
            "Payment cap — total ceiling across the term",
            "Deferment — qualifying events and evidence",
            "Term window — maximum calendar window to collect n payments",
            "Early settlement — formula and worked figure",
        ]),
        table("Scenario table — payment under each outcome",
              ["Post-programme income", "Monthly payment", "Months paid",
               "Total paid", "Vs. cap"], 5),
        cols(
            form("Scenario calculator inputs", [
                ("Expected starting income", "currency"),
                ("Expected months to employment", "number"),
                ("Expected annual raise", "percent"),
            ]),
            region("Calculator output region", [
                "Total expected payment",
                "Effective cost vs. sticker tuition",
                "Worst case (cap reached) / best case (floor never cleared)",
            ]),
        ),
        region("Provenance region — the transparency claim", [
            "Placement rate for this cohort family — figure, n, as-of date",
            "Median post-programme income — figure, n, as-of date",
            "Share of learners who never pay — figure, as-of date",
            "Verification source for each figure — link to exhibit",
            "Independent audit date and scope",
        ]),
        actions("Download terms as PDF", "Compare with loan equivalent",
                "Proceed to agreement"),
    ],
)

page(
    "learner-agreement", "Learner", "ISA agreement — review and sign",
    "What am I signing, and is this copy the binding one?",
    ["contracts", "verification", "ledger"],
    [
        region("Contract header region", [
            "Contract id and version hash",
            "Parties — learner, provider, funder",
            "Cohort id and start date",
            "Governing law and jurisdiction",
        ]),
        region("Clause reader region — scrollable, numbered clauses", [
            "1. Definitions",
            "2. Payment obligation and income share",
            "3. Income floor and deferment",
            "4. Payment cap and term window",
            "5. Verification and reporting duties",
            "6. Default, cure period, and dispute route",
            "7. Assignment and servicing",
            "8. Termination and refund window",
        ]),
        region("Key-terms sidebar — mirrors the transparency view", [
            "Income share, floor, cap, term — pinned while scrolling",
            "Diff marker against the terms page the learner reviewed",
        ]),
        form("Signature block", [
            ("Typed full legal name", "text"),
            ("Date", "date — server stamped"),
            ("I have read clauses 1–8", "checkbox"),
            ("I received the transparency view", "checkbox"),
            ("Two-factor code", "otp"),
        ]),
        actions("Sign agreement", "Download unsigned copy",
                "Request clause explanation", "Cancel"),
        note("Post-signature state swaps the signature block for: executed "
             "copy download, cooling-off period countdown, servicing contact."),
    ],
)

# --- employer flow --------------------------------------------------------
page(
    "employer-requisition", "Employer", "Requisition form",
    "What role am I hiring for, and which cohorts can fill it?",
    ["matching"],
    [
        form("Role definition", [
            ("Role title", "text"),
            ("Seniority", "select"),
            ("Location / remote policy", "select"),
            ("Headcount", "number"),
            ("Target start date", "date"),
        ]),
        form("Compensation", [
            ("Base salary range", "currency range"),
            ("Variable / bonus", "currency"),
            ("Contract type", "select — permanent, fixed term, apprenticeship"),
        ]),
        form("Requirements — feeds the match score", [
            ("Required skills", "multi-select — skill taxonomy"),
            ("Nice-to-have skills", "multi-select"),
            ("Minimum assessment score", "number"),
            ("Right-to-work requirement", "select"),
            ("Screening questions", "repeatable text"),
        ]),
        form("Commercial terms", [
            ("Placement fee model", "select — milestone, flat, none"),
            ("Agreed fee schedule", "select — links fee schedule page"),
            ("Billing contact", "email"),
            ("Purchase order reference", "text"),
        ]),
        actions("Publish requisition", "Save draft", "Preview matches",
                "Close requisition"),
        region("Preview region", [
            "Estimated matched-candidate count by cohort",
            "Estimated time to first interview",
            "Warning: no open cohort meets the skill set",
        ]),
    ],
)

page(
    "employer-matches", "Employer", "Matched candidate list",
    "Who fits this requisition, and how well?",
    ["matching", "verification"],
    [
        form("Filter bar", [
            ("Requisition", "select"),
            ("Minimum match score", "slider"),
            ("Cohort / provider", "multi-select"),
            ("Availability window", "date range"),
            ("Right-to-work verified only", "toggle"),
        ]),
        table("Candidate list",
              ["Candidate ref", "Match score", "Cohort", "Skills matched",
               "Assessment", "Availability", "Verified", "State"], 5),
        region("Candidate detail drawer", [
            "Anonymised profile until interview stage",
            "Skill evidence — assessment ids and scores",
            "Provider verification badge and date",
            "Score explanation — which requirement drove the score",
            "ISA disclosure notice — that a fee applies on placement",
        ]),
        actions("Request interview", "Shortlist", "Reject with reason",
                "Export list"),
        note("Reject reason is mandatory — it feeds the matching model and the "
             "provider outcome report."),
    ],
)

page(
    "employer-pipeline", "Employer", "Interview pipeline",
    "Where is every candidate, and what is blocking the next step?",
    ["matching", "reporting"],
    [
        tiles("Pipeline summary", [
            ("Open requisitions", "n"),
            ("In interview", "n"),
            ("Offers out", "n"),
            ("Placed this quarter", "n"),
        ]),
        region("Kanban region — columns, cards draggable", [
            "Column: Shortlisted",
            "Column: Interview scheduled",
            "Column: Interview complete",
            "Column: Offer issued",
            "Column: Offer accepted",
            "Column: Started — triggers placement milestone",
            "Column: Withdrawn / rejected",
        ]),
        region("Card face — per candidate", [
            "Candidate ref, requisition, match score",
            "Next action and owner",
            "Days in column, SLA breach marker",
            "Fee milestone that this column triggers",
        ]),
        form("Stage change", [
            ("New stage", "select"),
            ("Interview date and panel", "datetime + multi-select"),
            ("Outcome note", "textarea"),
            ("Start date (on acceptance)", "date — fires placement event"),
        ]),
        table("Event log", ["Timestamp", "Candidate", "From", "To", "Actor"], 3),
        actions("Advance stage", "Schedule interview", "Issue offer",
                "Record start date"),
    ],
)

page(
    "employer-fee-schedule", "Employer", "Milestone fee schedule",
    "What do I owe, when, and what fired it?",
    ["ledger", "contracts"],
    [
        region("Schedule header", [
            "Employer, agreement id, effective date",
            "Fee model — milestone percentages of first-year salary",
            "Clawback window and terms",
        ]),
        table("Milestones",
              ["Milestone", "Trigger event", "% of salary", "Amount",
               "Due date", "State"], 4),
        note("Milestones: offer accepted / start date reached / day-90 retained "
             "/ day-180 retained. Each trigger is a ledger event, not a manual "
             "entry."),
        table("Invoices",
              ["Invoice", "Candidate", "Milestone", "Amount", "Issued",
               "Paid", "State"], 4),
        tiles("Balance", [
            ("Invoiced to date", "currency"),
            ("Paid", "currency"),
            ("Outstanding", "currency"),
            ("Overdue", "currency"),
        ]),
        form("Dispute or adjustment", [
            ("Invoice", "select"),
            ("Reason", "select — no-show, early exit, wrong salary basis"),
            ("Evidence upload", "file"),
            ("Requested adjustment", "currency"),
        ]),
        actions("Pay invoice", "Download statement", "Raise dispute",
                "Update billing contact"),
    ],
)

# --- provider flow --------------------------------------------------------
page(
    "provider-cohort", "Provider", "Cohort creation",
    "What am I running, when, and on which ISA terms?",
    ["contracts", "matching"],
    [
        form("Cohort basics", [
            ("Cohort name", "text"),
            ("Programme / curriculum id", "select"),
            ("Start date", "date"),
            ("End date", "date"),
            ("Delivery mode", "select"),
            ("Location", "text"),
        ]),
        form("Capacity", [
            ("Total seats", "number"),
            ("ISA-funded seats", "number"),
            ("Self-funded seats", "number"),
            ("Application deadline", "date"),
            ("Minimum viable enrolment", "number"),
        ]),
        form("ISA terms template", [
            ("Terms template", "select — from contract template registry"),
            ("Income share", "percent"),
            ("Income floor", "currency"),
            ("Payment cap multiple", "number"),
            ("Term length (months)", "number"),
            ("Funder", "select"),
        ]),
        form("Outcome commitments — published on the transparency view", [
            ("Target placement rate", "percent"),
            ("Target median starting salary", "currency"),
            ("Reporting cadence", "select"),
        ]),
        actions("Create cohort", "Save draft", "Submit terms for approval",
                "Archive cohort"),
        region("Approval region", [
            "Funder approval state for the terms template",
            "Ops compliance check state",
            "Blocking issues list",
        ]),
    ],
)

page(
    "provider-seats", "Provider", "Seat inventory",
    "How many seats are sold, held, or at risk across my cohorts?",
    ["matching", "ledger"],
    [
        tiles("Inventory summary", [
            ("Open seats", "n"),
            ("Held seats", "n"),
            ("Filled seats", "n"),
            ("At-risk seats", "n"),
        ]),
        table("Seats by cohort",
              ["Cohort", "Start", "Total", "ISA-funded", "Held", "Filled",
               "Open", "Fill %"], 4),
        region("Seat detail region — one row per seat", [
            "Seat id and state — open, held, offered, signed, enrolled, released",
            "Hold expiry timestamp",
            "Learner ref once assigned",
            "Funder allocation reference",
        ]),
        form("Capacity adjustment", [
            ("Cohort", "select"),
            ("New total seats", "number"),
            ("New ISA-funded allocation", "number"),
            ("Reason", "textarea — audited"),
        ]),
        actions("Release expired holds", "Adjust capacity", "Reopen cohort",
                "Export inventory"),
        note("Hold expiry and release are ledger events — funder allocation "
             "must reconcile against seats sold."),
    ],
)

page(
    "provider-outcomes", "Provider", "Outcome reporting",
    "What happened to my graduates, and can I prove it?",
    ["reporting", "verification"],
    [
        region("Reporting period header", [
            "Cohort, period start and end, submission deadline",
            "Submission state — draft, submitted, under review, accepted",
        ]),
        table("Graduate outcomes",
              ["Learner ref", "Completion", "Employment state", "Employer",
               "Start salary", "Start date", "Evidence", "Verified"], 5),
        form("Bulk submission", [
            ("Outcome CSV upload", "file — template linked"),
            ("Evidence bundle", "file — offer letters, payslips"),
            ("Attestation by authorised signatory", "checkbox"),
            ("Signatory name and role", "text"),
        ]),
        tiles("Computed metrics — feed the transparency view", [
            ("Completion rate", "%"),
            ("Placement rate", "%"),
            ("Median starting salary", "currency"),
            ("Share never paying", "%"),
        ]),
        region("Validation region", [
            "Rows failing schema validation",
            "Rows contradicting ledger income events",
            "Rows lacking evidence — sent to the verification queue",
        ]),
        actions("Submit report", "Download template", "Fix flagged rows",
                "View published figures"),
    ],
)

page(
    "provider-success-fees", "Provider", "Success fees",
    "What has the ISA book earned me, and when is it paid?",
    ["ledger", "reporting"],
    [
        tiles("Earnings summary", [
            ("Collections this period", "currency"),
            ("Provider share", "currency"),
            ("Funder share", "currency"),
            ("Next payout date", "date"),
        ]),
        table("Fee events",
              ["Event", "Learner ref", "Cohort", "Collection", "Provider %",
               "Provider amount", "State"], 5),
        table("Payouts",
              ["Payout", "Period", "Gross", "Adjustments", "Net", "Paid on"], 3),
        region("Waterfall region — how a collection splits", [
            "Collection received",
            "Servicing cost deducted",
            "Funder principal and return",
            "Provider success share",
            "Reserve contribution",
        ]),
        form("Payout settings", [
            ("Bank account", "select"),
            ("Payout cadence", "select"),
            ("Minimum payout threshold", "currency"),
        ]),
        actions("Download remittance advice", "Reconcile period",
                "Query a fee event"),
        note("Provider share is derived from ledger collections only. No "
             "accrual view here — this page pays on cash received."),
    ],
)

# --- ops flow -------------------------------------------------------------
page(
    "ops-dashboard", "Ops", "Ops dashboard",
    "What is the book doing, and what needs a human today?",
    ["reporting", "ledger", "verification", "matching"],
    [
        tiles("Book health", [
            ("Active ISAs", "n"),
            ("In repayment", "n"),
            ("In deferment", "n"),
            ("In default", "n"),
        ]),
        tiles("This period", [
            ("Collections", "currency"),
            ("Placements", "n"),
            ("New agreements", "n"),
            ("Disputes opened", "n"),
        ]),
        region("Work queues region — each links to its page", [
            "Verification queue — count, oldest item age, SLA breaches",
            "Dispute cases — count by severity",
            "Failed collections — count, value",
            "Unmatched requisitions — count, age",
            "Overdue provider outcome reports — count",
        ]),
        region("Alert region", [
            "Reconciliation break — ledger vs. bank",
            "Cohort below minimum viable enrolment",
            "Funder covenant approaching breach",
            "Transparency figure stale beyond policy age",
        ]),
        table("Recent events", ["Time", "Type", "Entity", "Actor", "Detail"], 4),
        actions("Open verification queue", "Open disputes", "Open ledger",
                "Run reconciliation"),
    ],
)

page(
    "ops-verification-queue", "Ops", "Verification queue",
    "Which claims are unproven, and what evidence closes them?",
    ["verification"],
    [
        form("Queue filters", [
            ("Claim type", "multi-select — income, employment, identity, completion"),
            ("Age", "select"),
            ("Assigned to", "select"),
            ("SLA state", "select — within, at risk, breached"),
        ]),
        table("Queue",
              ["Case", "Claim type", "Subject", "Source", "Age", "SLA",
               "Assignee", "State"], 5),
        region("Case detail region", [
            "Claimed value vs. evidence value",
            "Evidence artefacts — document viewer, upload date, hash",
            "Third-party check result — payroll, tax, employer confirmation",
            "Conflict markers against ledger and provider report",
            "Decision history and reviewer notes",
        ]),
        form("Decision", [
            ("Outcome", "radio — verified, rejected, needs more evidence"),
            ("Verified value", "currency or text"),
            ("Evidence reference", "text"),
            ("Reviewer note", "textarea"),
            ("Second reviewer required", "checkbox — above threshold"),
        ]),
        actions("Record decision", "Request evidence", "Escalate to dispute",
                "Reassign"),
        note("A verified income decision writes the payment basis to the "
             "ledger. Rejections above threshold open a dispute case."),
    ],
)

page(
    "ops-disputes", "Ops", "Dispute cases",
    "What is contested, by whom, and what is the clock?",
    ["verification", "contracts", "ledger"],
    [
        tiles("Dispute load", [
            ("Open cases", "n"),
            ("Breaching SLA", "n"),
            ("Value at issue", "currency"),
            ("Median days to close", "n"),
        ]),
        table("Case list",
              ["Case", "Raised by", "Type", "Counterparty", "Value", "Opened",
               "SLA", "Stage"], 5),
        region("Case file region", [
            "Claim statement and clause cited",
            "Timeline — every message, decision, and deadline",
            "Evidence from both sides",
            "Linked ledger entries frozen pending outcome",
            "Escalation path — internal review, external adjudicator",
        ]),
        form("Case action", [
            ("Stage", "select — intake, investigation, decision, appeal, closed"),
            ("Determination", "select — upheld, partly upheld, rejected"),
            ("Ledger adjustment", "currency — writes a correcting entry"),
            ("Rationale", "textarea — disclosed to both parties"),
            ("Next deadline", "date"),
        ]),
        actions("Record determination", "Message parties", "Freeze collections",
                "Close case"),
    ],
)

page(
    "ops-ledger", "Ops", "Ledger view",
    "Where did every pound come from and go, and does it balance?",
    ["ledger"],
    [
        form("Ledger filters", [
            ("Account", "select — learner, provider, funder, employer, reserve"),
            ("Entry type", "multi-select — collection, fee, payout, adjustment"),
            ("Date range", "date range"),
            ("Entity", "search"),
            ("Show reversed entries", "toggle"),
        ]),
        table("Entries",
              ["Entry id", "Date", "Type", "Debit account", "Credit account",
               "Amount", "Source event", "State"], 6),
        tiles("Balances", [
            ("Collections to date", "currency"),
            ("Funder payable", "currency"),
            ("Provider payable", "currency"),
            ("Unreconciled", "currency"),
        ]),
        region("Reconciliation region", [
            "Bank statement import and match rate",
            "Unmatched bank lines",
            "Unmatched ledger entries",
            "Break ageing and owner",
        ]),
        region("Entry detail region", [
            "Immutable entry with source event id",
            "Contract clause that authorised it",
            "Reversal chain if corrected",
        ]),
        actions("Post adjustment", "Import bank file", "Export period",
                "Lock period"),
        note("Entries are append-only. Corrections post a reversal plus a new "
             "entry; nothing is edited in place."),
    ],
)

page(
    "ops-funder-dashboard", "Ops", "Funder dashboard",
    "Is the portfolio performing against what the funder was promised?",
    ["reporting", "ledger"],
    [
        tiles("Portfolio", [
            ("Capital deployed", "currency"),
            ("Capital returned", "currency"),
            ("Active contracts", "n"),
            ("Weighted avg. term remaining", "months"),
        ]),
        tiles("Performance", [
            ("Realised multiple", "x"),
            ("Projected multiple", "x"),
            ("Default rate", "%"),
            ("Deferment rate", "%"),
        ]),
        table("Vintage performance",
              ["Cohort vintage", "Contracts", "Deployed", "Collected",
               "Placement %", "Multiple to date"], 5),
        region("Chart region — SVG, no chart framework", [
            "Collections by month — bar",
            "Cumulative deployed vs. returned — line",
            "Contract state mix over time — stacked bar",
        ]),
        region("Covenant region", [
            "Covenant, threshold, current value, headroom, state",
            "Breach history and cure actions",
        ]),
        form("Capital call / drawdown", [
            ("Facility", "select"),
            ("Amount", "currency"),
            ("Allocation to cohorts", "multi-select"),
            ("Requested value date", "date"),
        ]),
        actions("Issue capital call", "Export funder report",
                "Download loan tape", "Open ledger"),
    ],
)


# ---------- render --------------------------------------------------------
PAGE_TMPL = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ISA wireframe — {title}</title>
<style>{css}</style>
<div class="page">
<div class="crumb"><a href="index.html">ISA production wireframes</a>
 / {flow} flow / {title}</div>
<h1>{title}</h1>
<p class="q">Question this page answers: {question}</p>
{body}
<footer>Wireframe only — greybox, no visual design.
Backed by wave-2 module: {modules}</footer>
</div>
</html>
"""


def render_page(p):
    mods = " ".join("<b>%s</b>" % esc(MODULES[m]) for m in p["modules"])
    return PAGE_TMPL.format(
        title=esc(p["title"]),
        flow=esc(p["flow"]),
        question=esc(p["question"]),
        css=CSS,
        body="\n".join(p["blocks"]),
        modules=mods,
    )


INDEX_TMPL = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ISA production wireframes</title>
<style>{css}</style>
<div class="page">
<div class="crumb">internal portal / ventures / ISA / wireframes</div>
<h1>ISA production wireframes</h1>
<p class="q">Every page the live ISA site needs to be functional, as a
greybox wireframe. {n} pages across four flows. Each page names the wave-2
module that backs it.</p>
{body}
<div class="box"><div class="lbl">Wave-2 modules referenced</div>
<ul class="items">
<li><b>matching</b> — requisitions, candidate scoring, seat assignment</li>
<li><b>contracts</b> — terms templates, agreement generation, signature, clauses</li>
<li><b>ledger</b> — append-only money events, collections, payouts, reconciliation</li>
<li><b>verification</b> — identity, income, employment and completion claims</li>
<li><b>reporting</b> — outcome reports, transparency figures, funder reporting</li>
</ul></div>
<footer>Greybox wireframes. No visual design, no copy, no live data.</footer>
</div>
</html>
"""


def render_index():
    flows = []
    for flow in ["Learner", "Employer", "Provider", "Ops"]:
        items = []
        for p in PAGES:
            if p["flow"] != flow:
                continue
            mods = ", ".join(p["modules"])
            items.append(
                '<li><a href="%s.html">%s</a> — %s <span class="t">[%s]</span></li>'
                % (esc(p["slug"]), esc(p["title"]), esc(p["question"]), esc(mods))
            )
        flows.append(
            '<div class="box"><div class="lbl">%s flow</div>'
            '<ul class="items">%s</ul></div>' % (esc(flow), "".join(items))
        )
    return INDEX_TMPL.format(css=CSS, body="\n".join(flows), n=len(PAGES))


def main():
    for p in PAGES:
        path = os.path.join(OUT, p["slug"] + ".html")
        with open(path, "w") as f:
            f.write(render_page(p))
        print("wrote", os.path.basename(path))
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(render_index())
    print("wrote index.html (%d pages)" % len(PAGES))


if __name__ == "__main__":
    main()
