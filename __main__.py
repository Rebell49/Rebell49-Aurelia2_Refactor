
from __future__ import annotations
import click
from .resource_manager import ResourceManager
from .thought_stream import ThoughtStream
from .archive_manager import ArchiveManager
from .ui import run_ui

@click.group(help="Aurelia² – neugierig, empathisch, fokussiert.")
def cli():
    pass

@cli.command()
@click.argument("text", nargs=-1)
def think(text):
    "Einen Gedanken speichern."
    ts = ThoughtStream()
    t = ts.add(" ".join(text))
    click.echo(f"OK {t.ts} tokens={len(t.tokens)}")

@cli.command()
def status():
    "Status & Kennzahlen anzeigen."
    rm = ResourceManager()
    snap = rm.snapshot()
    ts = ThoughtStream()
    stats = ts.stats()
    click.echo(f"System: cpu={snap['cpu']}% mem={snap['mem_percent']}%")
    click.echo(f"Gedanken: entries={stats['entries']} avg_tokens={stats['avg_tokens']:.1f}")

@cli.command()
@click.argument("zip_path")
def export(zip_path):
    "Alle Daten als ZIP exportieren."
    am = ArchiveManager()
    out = am.export_zip(zip_path)
    click.echo(f"Exportiert: {out}")

@cli.command()
def ui():
    "Einfache Kivy-UI starten."
    run_ui()

if __name__ == "__main__":
    cli()
