# Delete Multiple Entities

Delete multiple Onfleet entities (workers, tasks, admins, teams, or webhooks) in bulk via an interactive web UI or directly via the command-line script.

This tool is part of the [Onfleet Developer open source repository](https://github.com/onfleet/developer) — a collection of resources and tools to augment and accelerate custom integrations with the Onfleet API.

> **Note:** All scripts require Python 3.

## Table of Contents

- [Disclaimer](#disclaimer)
- [Files](#files)
- [Web UI (recommended)](#web-ui-recommended)
  - [Installation](#installation)
  - [Running locally](#running-locally)
  - [Usage](#usage)
- [Command-line script](#command-line-script)
- [Dependencies](#dependencies)
- [Related resources](#related-resources)

---

## Disclaimer

**This tool does not have a rollback function. Any deletion cannot be reversed.**
Please double-check your inputs before executing. Onfleet is not responsible for any loss of data resulting from the use of this tool.

---

## Files

| File | Description |
|------|-------------|
| `app.py` | Flask web server — serves the UI and proxies delete requests to the Onfleet API |
| `templates/index.html` | Browser-based UI |
| `deletion.py` | Original command-line script for manual use |

---

## Web UI (recommended)

### Installation

1. Clone the repository and navigate to this folder:

```bash
git clone https://github.com/onfleet/developer.git
cd developer/api-tools/delete-entities
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running locally

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

> **Debug mode:** Debug mode is **off by default**. Never enable it on a shared or internet-facing machine — it exposes an interactive Python debugger that allows arbitrary code execution. To turn it on temporarily during local development only:
>
> ```bash
> # macOS/Linux
> FLASK_DEBUG=1 python app.py
>
> # Windows (Command Prompt)
> set FLASK_DEBUG=1 && python app.py
>
> # Windows (PowerShell)
> $env:FLASK_DEBUG="1"; python app.py
> ```
>
> Leave `FLASK_DEBUG` unset (or set to `0`) for normal use.

### Usage

1. **API Key** — Enter your Onfleet API key. For help creating one, see the [Onfleet API key guide](https://support.onfleet.com/hc/en-us/articles/360045763292-API#h_01FTGN2E1AGNAA4DB3Q2RPVWD9).
2. **Entity Type** — Select the type of entity to delete: Workers, Tasks, Admins, Teams, or Webhooks.
3. **IDs to Delete** — Paste one entity ID per line.
4. Click **Delete** — all fields are validated before submission. A confirmation dialog will appear reminding you that deletions are permanent.
5. Results stream in live as each deletion is processed. Any errors are shown inline without stopping the remaining deletions.
6. A final summary shows total succeeded and failed counts.

---

## Command-line script

If you prefer to run without the UI, edit `deletion.py` directly:

1. Set `ENTITY` to the entity type (e.g. `tasks`, `workers`).
2. Set `USERNAME` to your Onfleet API key.
3. Populate `id_list` with the IDs to delete.
4. Run:

```bash
pip install requests
python deletion.py
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Local web server and UI |
| `requests` | HTTP requests to the Onfleet API |

---

## Related resources

- [Onfleet API documentation](https://docs.onfleet.com/reference#introduction)
- [Onfleet API key setup](https://support.onfleet.com/hc/en-us/articles/360045763292-API#h_01FTGN2E1AGNAA4DB3Q2RPVWD9)
- `pyonfleet` — Onfleet Python API wrapper: [repository](https://github.com/onfleet/pyonfleet) · [PyPI](https://pypi.org/project/pyonfleet/)
- `node-onfleet` — Onfleet Node.js API wrapper: [repository](https://github.com/onfleet/node-onfleet)
