# Tropicana SIC Prototype

Test page for evaluating whether the rich SAP PM export (54 columns) can pre-fill
the Shift Availability Report (SIC) that supervisors currently fill in by hand.

## What's wired

- **📊 Generate SIC Report** button in the header (next to the shift report button)
- Modal with: date picker, day/night tabs, regenerate, copy plain text, download HTML
- Heavy fleet Y/N pre-fill from `still_down` events
- Status mapping from notification title keywords:
  - PARTS / WAITING / STOCK / JPF / DNF → "Waiting on Parts"
  - 12W / 2W / 4W / 500H / 3000H → "In for Service"
  - default → "Repairs Ongoing"
- Equipment descriptions derived from `Functional Location` code prefix
  (LOBG* → LOADER BOGGER, TKDM* → TRUCK DUMP, etc.)
- Daily services auto-tint: 4 cells per asset (Day 12h / Night 12h / Day 24h / Night 24h)
  coloured from `Daily *N` and `*PM SERVICE` notifications
- Plain-text export ready to paste into Outlook

## What's still manual

- Light vehicles section (no SAP data)
- "D/S" / "N/S" planning rows (rows 5-6 of the SIC sheet)
- Supervisor override of any auto-tint (no click-to-force-missed yet)

## Build

Static, no build step. Open `index.html` directly or serve with any HTTP server.
