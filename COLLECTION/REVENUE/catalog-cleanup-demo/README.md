# Catalog cleanup pilot — synthetic demonstration

This folder is a **fictional sample**, not client work and not a claim of real customer results. All product names and example.invalid URLs are synthetic.

## What it demonstrates
- Preserve an immutable copy of the input.
- Normalize title whitespace and prices only where the source supplies a currency.
- Remove one exact duplicate from the cleaned output while documenting it.
- Flag missing SKU, missing price, ambiguous availability, and missing currency.
- Never invent product specifications, prices, currency, availability, or brand claims.

## Files
- INPUT_SYNTHETIC.csv — intentionally messy 10-row input.
- CLEANED_SYNTHETIC.csv — 9 unique product records with explicit data-quality status.
- The output uses a placeholder label for the missing-SKU row; it is not represented as a real SKU.

## Acceptance checks
1. The source input remains unchanged.
2. Each transformed field has a reason in data_quality_notes.
3. Unknown values remain unknown and are flagged.
4. Exact duplicate handling is disclosed.
5. The buyer approves the two-row sample before the remaining catalog is processed.

## Commercial boundary
Offer a small paid pilot only after scope, acceptance criteria, and a usable payment method are agreed. This sample does not prove revenue, client demand, or any increase in sales.
