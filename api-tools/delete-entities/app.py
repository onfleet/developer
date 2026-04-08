import html
import json
import time

import requests
from flask import Flask, Response, render_template, request, stream_with_context

app = Flask(__name__)

API_URL = "https://onfleet.com/api/v2"
VALID_ENTITIES = {"workers", "tasks", "admins", "teams", "webhooks"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/delete", methods=["POST"])
def delete_entities():
    data = request.get_json()
    api_key = (data.get("api_key") or "").strip()
    entity = (data.get("entity") or "").strip()
    ids = [i.strip() for i in (data.get("ids") or []) if i.strip()]

    if not api_key:
        return {"error": "API key is required."}, 400
    if entity not in VALID_ENTITIES:
        return {"error": f"Invalid entity '{html.escape(entity)}'."}, 400
    if not ids:
        return {"error": "No valid IDs provided."}, 400

    def generate():
        for entity_id in ids:
            try:
                url = f"{API_URL}/{entity}/{entity_id}"
                resp = requests.delete(url, auth=(api_key, ""), timeout=10)
                resp.raise_for_status()
                result = {"id": entity_id, "status": "success", "message": "Deleted successfully"}
            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code if e.response is not None else "?"
                result = {
                    "id": entity_id,
                    "status": "error",
                    "message": f"HTTP {status_code}: {e.response.text if e.response is not None else str(e)}",
                }
            except requests.exceptions.RequestException as e:
                result = {"id": entity_id, "status": "error", "message": str(e)}

            yield f"data: {json.dumps(result)}\n\n"
            time.sleep(1)

        yield f"data: {json.dumps({'done': True})}\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
