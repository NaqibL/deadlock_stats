"""Writing the outputs: CSVs, the spreadsheet and the build report."""
from __future__ import annotations

import csv
from pathlib import Path

TABLES = ("heroes", "abilities", "items", "investment", "progression", "units", "rules", "powerups",
          "permanent_buffs", "meta")


def cell(value):
    """CSV representation: blank for "not applicable", plain numbers, no units."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    return value


def write_csv(path: Path, columns, rows) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, lineterminator="\n")
        writer.writerow(columns)
        for row in rows:
            writer.writerow([cell(row.get(column)) for column in columns])


def read_csv(path: Path) -> list:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_xlsx(path: Path, sheets) -> None:
    """``sheets`` is a list of ``(title, columns, rows)``. Numbers are stored as numbers."""
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    workbook = Workbook()
    workbook.remove(workbook.active)
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill("solid", fgColor="2F3B52")
    for title, columns, rows in sheets:
        sheet = workbook.create_sheet(title)
        sheet.append(list(columns))
        for row in rows:
            sheet.append([None if row.get(c) is None else row.get(c) for c in columns])
        for index, column in enumerate(columns, start=1):
            head = sheet.cell(row=1, column=index)
            head.font, head.fill = header_font, header_fill
            head.alignment = Alignment(vertical="center")
            longest = max([len(str(column))] + [len(str(r.get(column))) for r in rows if r.get(column) is not None])
            sheet.column_dimensions[get_column_letter(index)].width = min(max(longest + 2, 8), 60)
        sheet.freeze_panes = "C2" if len(columns) > 2 else "A2"
        if rows:
            sheet.auto_filter.ref = sheet.dimensions
    workbook.save(path)


def write_outputs(out_dir: Path, tables: dict) -> None:
    """``tables`` maps table name -> ``(columns, rows)``."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in TABLES:
        columns, rows = tables[name]
        write_csv(out_dir / f"{name}.csv", columns, rows)
    write_xlsx(out_dir / "deadlock.xlsx", [(name.replace("_", " ").capitalize(), *tables[name]) for name in TABLES])
