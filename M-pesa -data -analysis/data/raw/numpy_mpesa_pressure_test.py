"""
numpy_mpesa_pressure_test.py - 10 numpy questions on YOUR M-PESA statement.



THE QUESTION BANK
  Q1  Totals and net                      (Excel: SUM)
  Q2  Count money-in vs money-out         (Excel: COUNTIF)
  Q3  Five biggest outflows               (Excel: LARGE / sort)
  Q4  Mean vs median outflow, top-10 share
  Q5  Categorise every row                (Excel: nested IF + SEARCH)
  Q6  Money out per category              (Excel: SUMIF)
  Q7  Money out per month                 (Excel: TEXT + SUMIF)
  Q8  Money out per weekday               (datetime arithmetic)
  Q9  Does Balance reconcile?             (cumulative logic with diff)
  Q10 Stress test: Python loop vs numpy   (1.2 million rows)
"""

import time
import numpy as np
import pandas as pd

# ----------------------------- SETTINGS ------------------------------------
CSV_PATH = r"C:\Users\wanga\OneDrive\Desktop\Projects\excellent-data\M-pesa -data -analysis\data\raw\MPESA_Statement _2026(processed).csv"
SKIP_ROWS = 0
COL = {
    "time": "Completion Time",
    "details": "Details",
    "paid_in": "Paid In",
    "withdrawn": "Withdrawn",
    "balance": "Balance",
}
# Your Dashboard numbers, after cleaning the junk rows. Set to None to skip.
EXPECTED = {"money_in": 165120.13, "money_out": 161561.22}
TOL = 0.01
DAY_FIRST = True   # tie-breaker only: used if every date is ambiguous (day <= 12)

# Same order as your final nested IF. First match wins.
RULES = [
    ("bundle", "Bundles"), ("airtime", "Bundles"),
    ("merchant", "Merchant Payment"), ("offnet c2b", "Merchant Payment"),
    ("offnet b2c", "Merchant Payment"), ("customer payment to small", "Merchant Payment"),
    ("payment to small business", "Merchant Payment"),
    ("sent to", "Sent to Person"), ("customer transfer to", "Sent to Person"),
    ("business payment", "Money In"), ("funds received", "Money In"),
    ("receive international", "Money In"), ("send money reversal", "Money In"),
    ("pay utility reversal", "Money In"), ("customer transfer", "Money In"),
    ("ziidi", "Investment"), ("nabo", "Investment"),
    ("paybill online", "Pay Bill"), ("pay bill", "Pay Bill"), ("spotify", "Pay Bill"),
    ("m-shwari", "Mshwari"), ("mshwari", "Mshwari"),
    ("withdrawal charge", "Fees"), ("customer withdrawal", "Fees"), ("charge", "Fees"),
]
# ---------------------------------------------------------------------------


# =============================== LOADER ====================================
def _to_number(series):
    cleaned = series.astype(str).str.replace(",", "", regex=False).str.strip()
    return pd.to_numeric(cleaned, errors="coerce")


def _detect_sep(path):
    """Look at the header line and pick the separator it uses: comma, tab or semicolon."""
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        header = ""
        for _ in range(SKIP_ROWS + 1):
            header = f.readline()
    counts = {sep: header.count(sep) for sep in [",", "\t", ";"]}
    return max(counts, key=counts.get)


def load():
    """Read the CSV and return a dict of numpy arrays, sorted oldest to newest."""
    sep = _detect_sep(CSV_PATH)
    df = pd.read_csv(CSV_PATH, skiprows=SKIP_ROWS, sep=sep, encoding_errors="replace")
    print(f"Separator detected: {'TAB' if sep == chr(9) else repr(sep)}")
    df.columns = df.columns.astype(str).str.strip()
    missing = [v for v in COL.values() if v not in df.columns]
    if missing:
        raise KeyError(f"Columns not found: {missing}. Your file has: {list(df.columns)}")

    raw_time = df[COL["time"]].astype(str).str.strip()
    day_first_formats = ["%d/%m/%Y %I:%M:%S %p", "%m/%d/%Y %I:%M:%S %p"]
    formats = (day_first_formats if DAY_FIRST else day_first_formats[::-1]) + [
        "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%m/%d/%Y %H:%M:%S",
    ]
    best, best_rate = None, -1.0
    for fmt in formats:
        parsed = pd.to_datetime(raw_time, format=fmt, errors="coerce")
        rate = parsed.notna().mean()
        if rate > best_rate:          # ties keep the earlier (preferred) format
            best, best_rate = parsed, rate

    paid = _to_number(df[COL["paid_in"]])
    out = _to_number(df[COL["withdrawn"]]).abs()   # some exports show withdrawals as negatives
    bal = _to_number(df[COL["balance"]])

    valid = best.notna()
    dropped = ~valid
    money_on_dropped = float(np.nansum(paid[dropped]) + np.nansum(out[dropped]))
    order = np.argsort(best[valid].to_numpy().astype("datetime64[s]"), kind="stable")

    def pick(series):
        return series[valid].to_numpy(dtype=float)[order]

    dates = best[valid].to_numpy().astype("datetime64[s]")[order]
    details = np.array(df.loc[valid, COL["details"]].astype(str).tolist(), dtype=str)[order]

    d = {
        "dates": dates,
        "details": details,
        "paid_in": pick(paid),
        "withdrawn": pick(out),
        "balance": pick(bal),
    }
    d["n"] = len(d["dates"])

    print("=" * 70)
    print(f"Loaded {d['n']:,} transactions. Dropped {int(dropped.sum())} rows with no valid date "
          f"(money sitting on them: {money_on_dropped:,.2f}).")
    print(f"Date range: {dates.min()} to {dates.max()}   <- should be Jan to May 2026. "
          f"If not, flip DAY_FIRST.")
    print("=" * 70)
    return d


# ============================= REFERENCE LOGIC =============================
# Slow, plain-Python versions the checks compare against. Don't peek until
# you've tried each question!
def reference_category(details):
    out = []
    for text in details:
        t = text.lower()
        for kw, cat in RULES:
            if kw in t:
                out.append(cat)
                break
        else:
            out.append("Other")
    return np.array(out)


# ============================ YOUR QUESTIONS ===============================
# Each takes `d` (dict of numpy arrays: dates, details, paid_in, withdrawn,
# balance, n). d["category"] is also provided for Q6.

def q1_totals(d):
    """Return (money_in, money_out, net).
    TRAP: blank cells are NaN. What does np.sum do with NaN? Find the safe one."""
    raise NotImplementedError


def q2_counts(d):
    """Return (number_of_money_in_rows, number_of_money_out_rows).
    A money-in row has Paid In > 0; a money-out row has Withdrawn > 0.
    Hint: a comparison gives a True/False array; True counts as 1."""
    raise NotImplementedError


def q3_top5(d):
    """Return the 5 biggest outflow amounts, largest first, as an array.
    TRAP: np.sort / np.argsort put NaN at the END. A naive 'last 5' picks NaN."""
    raise NotImplementedError


def q4_typical(d):
    """Return (mean_outflow, median_outflow, top10_share_percent).
    Use only rows where Withdrawn > 0. top10_share = the 10 biggest outflows
    as a % of total outflow. Which is more 'typical': mean or median? Why?"""
    raise NotImplementedError


def q5_categories(d):
    """Return an array of category names, one per row, using RULES (first match wins).
    This is your nested IF + SEARCH, vectorised. Hint: np.char.lower,
    np.char.find(...) >= 0 for each keyword, then np.select(conditions, choices,
    default='Other')."""
    raise NotImplementedError


def q6_by_category(d):
    """Return {category: total_money_out} using d['category'].
    Excel's SUMIF. Hint: np.unique(..., return_inverse=True) then np.bincount
    with weights=. TRAP: NaN in weights makes the whole total NaN."""
    raise NotImplementedError


def q7_by_month(d):
    """Return {'2026-01': total_money_out, ...}.
    Hint: d['dates'].astype('datetime64[M]') turns timestamps into months."""
    raise NotImplementedError


def q8_by_weekday(d):
    """Return an array of 7 totals: Monday first, Sunday last.
    Hint: d['dates'].astype('datetime64[D]').astype(int) counts days since
    1 Jan 1970, which was a THURSDAY. Use % 7 and shift so Monday = 0."""
    raise NotImplementedError


def q9_balance_breaks(d):
    """Return how many rows break this rule:
         balance[i] - balance[i-1] == paid_in[i] - withdrawn[i]   (within 0.01)
    for i = 1..n-1. Hint: np.diff. A few breaks may be real (same-second ties,
    reversals) - what would you do about a large number?"""
    raise NotImplementedError


def q10_stress(d):
    """Repeat the withdrawn column 1000 times (np.tile) to make ~1.2 million rows.
    Sum it with a plain Python for-loop, then with np.sum, timing both with
    time.perf_counter(). Return (loop_seconds, numpy_seconds)."""
    raise NotImplementedError


# =============================== CHECKS ====================================
def _ser(a):
    return pd.Series(a)


def check_q1(res, d):
    mi, mo, net = res
    if EXPECTED is None:
        return "INFO", f"in={mi:,.2f} out={mo:,.2f} net={net:,.2f}"
    ok = (abs(mi - EXPECTED["money_in"]) <= TOL and abs(mo - EXPECTED["money_out"]) <= TOL
          and abs(net - (mi - mo)) <= TOL)
    return ("PASS" if ok else "FAIL",
            f"in={mi:,.2f} out={mo:,.2f} net={net:,.2f} "
            f"(expected in={EXPECTED['money_in']:,.2f}, out={EXPECTED['money_out']:,.2f})")


def check_q2(res, d):
    ref = (int((_ser(d["paid_in"]) > 0).sum()), int((_ser(d["withdrawn"]) > 0).sum()))
    return ("PASS" if tuple(res) == ref else "FAIL"), f"yours={tuple(res)} reference={ref}"


def check_q3(res, d):
    ref = _ser(d["withdrawn"]).nlargest(5).to_numpy()
    ok = len(res) == 5 and np.allclose(res, ref)
    return ("PASS" if ok else "FAIL"), f"yours={np.round(res, 2)} reference={np.round(ref, 2)}"


def check_q4(res, d):
    s = _ser(d["withdrawn"])
    s = s[s > 0]
    ref = (s.mean(), s.median(), s.nlargest(10).sum() / s.sum() * 100)
    ok = np.allclose(res, ref, atol=0.01)
    return ("PASS" if ok else "FAIL"), (f"mean={res[0]:,.2f} median={res[1]:,.2f} "
                                          f"top10={res[2]:.1f}% (reference {ref[0]:,.2f}/{ref[1]:,.2f}/{ref[2]:.1f}%)")


def check_q5(res, d):
    ref = reference_category(d["details"])
    res = np.asarray(res)
    ok = len(res) == len(ref) and bool(np.all(res == ref))
    n_other = int(np.sum(res == "Other")) if len(res) else -1
    return ("PASS" if ok else "FAIL"), f"matches reference: {ok}; rows left as 'Other': {n_other}"


def check_q6(res, d):
    s = _ser(d["withdrawn"]).groupby(d["category"]).sum()
    keys = set(res) | set(s.index)
    ok = all(abs(res.get(k, 0) - s.get(k, 0)) <= TOL for k in keys)
    total = sum(res.values())
    return ("PASS" if ok else "FAIL"), f"sum of categories={total:,.2f}"


def check_q7(res, d):
    months = pd.Series(d["dates"]).dt.to_period("M").astype(str)
    s = _ser(d["withdrawn"]).groupby(months.to_numpy()).sum()
    keys = set(res) | set(s.index)
    ok = all(abs(res.get(k, 0) - s.get(k, 0)) <= TOL for k in keys)
    total = sum(res.values())
    note = ""
    if EXPECTED:
        gap = EXPECTED["money_out"] - total
        note = f" | gap to Dashboard total: {gap:,.2f}"
    return ("PASS" if ok else "FAIL"), f"monthly sum={total:,.2f}{note}"


def check_q8(res, d):
    dow = pd.Series(d["dates"]).dt.dayofweek
    ref = _ser(d["withdrawn"]).groupby(dow.to_numpy()).sum().reindex(range(7), fill_value=0).to_numpy()
    ok = len(res) == 7 and np.allclose(res, ref, atol=TOL)
    names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return ("PASS" if ok else "FAIL"), " ".join(f"{n}={v:,.0f}" for n, v in zip(names, res))


def check_q9(res, d):
    bal = _ser(d["balance"])
    flow = _ser(d["paid_in"]).fillna(0) - _ser(d["withdrawn"]).fillna(0)
    step = bal.diff()
    ref = int((((step - flow).abs() > 0.01) & step.notna()).iloc[1:].sum())
    return ("PASS" if int(res) == ref else "FAIL"), (f"breaks={int(res)} of {d['n'] - 1:,} "
                                                      f"({int(res) / max(d['n'] - 1, 1) * 100:.1f}%), reference={ref}")


def check_q10(res, d):
    loop_s, np_s = res
    ok = np_s < loop_s
    return ("PASS" if ok else "FAIL"), (f"loop={loop_s:.3f}s numpy={np_s:.5f}s "
                                         f"-> numpy is ~{loop_s / max(np_s, 1e-9):,.0f}x faster")


QUESTIONS = [
    ("Q1  Totals and net", "q1_totals", check_q1),
    ("Q2  Counts", "q2_counts", check_q2),
    ("Q3  Top 5 outflows", "q3_top5", check_q3),
    ("Q4  Mean vs median", "q4_typical", check_q4),
    ("Q5  Categorise rows", "q5_categories", check_q5),
    ("Q6  By category", "q6_by_category", check_q6),
    ("Q7  By month", "q7_by_month", check_q7),
    ("Q8  By weekday", "q8_by_weekday", check_q8),
    ("Q9  Balance breaks", "q9_balance_breaks", check_q9),
    ("Q10 Stress test", "q10_stress", check_q10),
]


def run_all(d, impl=None):
    """Run every question. impl = dict of functions (defaults to this file's)."""
    impl = impl if impl is not None else globals()
    d["category"] = reference_category(d["details"])   # provided for Q6
    passed = todo = 0
    for label, fname, checker in QUESTIONS:
        try:
            result = impl[fname](d)
            status, msg = checker(result, d)
        except NotImplementedError:
            status, msg = "TODO", "not attempted yet"
        except Exception as e:                       # show the error, keep going
            status, msg = "ERROR", f"{type(e).__name__}: {e}"
        passed += status in ("PASS", "INFO")
        todo += status == "TODO"
        print(f"{label:<22} {status:<6} {msg}")
    print("-" * 70)
    print(f"{passed}/{len(QUESTIONS)} passed, {todo} still TODO")


if __name__ == "__main__":
    run_all(load())