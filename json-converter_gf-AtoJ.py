#!/usr/bin/env python3

import json
import sys
import os
import argparse

"""
Usage:
    python json_converter_gf-AtoJ.py --all
        Processes all *.json files in the current directory.

    python json_converter_gf-AtoJ.py -f <input_json>
        Processes a single file.

The script will:
1) Load the JSON from the specified file(s).
2) Look under the top-level key "0" for "confirmations" and "notifications" arrays, and a "title" field.
3) Preserve the original IDs for each confirmation and notification.
4) Replace each with the updated structure specified.
5) Write out the new JSON to a filename based on the form's title.
"""


def process_file(input_file: str) -> None:
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    # Load the JSON
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading '{input_file}': {e}")
        return

    if "0" not in data:
        print(f"Error: The JSON in '{input_file}' does not contain the expected '0' key.")
        return

    form_data = data["0"]

    # Verify that we have the necessary keys
    required_keys = ["title", "confirmations", "notifications"]
    for key in required_keys:
        if key not in form_data:
            print(f"Error: The JSON in '{input_file}' does not have the '{key}' key under '0'.")
            return

    # Extract the original IDs from confirmations and notifications
    original_confirmations = form_data["confirmations"]
    original_notifications = form_data["notifications"]

    if len(original_confirmations) == 0:
        print(f"Warning: No confirmations found to replace in '{input_file}'.")
    if len(original_notifications) < 2:
        print(f"Warning: Less than two notifications found in '{input_file}'.")

    # We'll just take the first confirmation's ID and the first two notifications' IDs
    # (based on the example snippet). Adjust if the JSON structure differs.
    if len(original_confirmations) > 0:
        confirm_id = original_confirmations[0].get("id", "")
    else:
        confirm_id = ""

    notif_id_1 = ""
    notif_id_2 = ""

    if len(original_notifications) > 0:
        notif_id_1 = original_notifications[0].get("id", "")
    if len(original_notifications) > 1:
        notif_id_2 = original_notifications[1].get("id", "")

    # Replace confirmations
    new_confirmations = [
        {
            "id": confirm_id,
            "name": "Standard Bestätigung",
            "isDefault": True,
            "type": "message",
            "message": (
                "Vielen Dank für Ihr Interesse!\r\n\r\n"
                "Eine Bestätigung Ihrer Anfrage erhalten Sie in den nächsten Minuten per Mail."
            ),
            "url": "",
            "pageId": "",
            "queryString": "",
            "event": "",
            "disableAutoformat": False,
            "page": "",
            "conditionalLogic": []
        }
    ]

    # Replace notifications
    new_notifications = []

    # Administrator-Benachrichtigung
    new_notifications.append({
        "id": notif_id_1,
        "isActive": True,
        "to": "verkauf@juenemann-instruments.de",
        "name": "Administrator-Benachrichtigung",
        "event": "form_submission",
        "toType": "email",
        "subject": "Neue Anfrage über Website",
        "message": "{form_title}\r\n\r\n{all_fields}",
        "service": "wordpress",
        "toEmail": "verkauf@juenemann-instruments.de",
        "routing": None,
        "fromName": "",
        "from": "info@juenemann-instruments.de",
        "replyTo": "",
        "bcc": "simon.koelling@armatherm.de, {admin_email}",
        "disableAutoformat": False,
        "notification_conditional_logic_object": "",
        "notification_conditional_logic": "0",
        "conditionalLogic": None,
        "cc": "",
        "enableAttachments": False,
        "toField": "",
        "gfacl_prepared_notifications": True
    })

    # Kunden Mail
    new_notifications.append({
        "id": notif_id_2,
        "name": "Kunden Mail",
        "service": "wordpress",
        "event": "form_submission",
        "toType": "field",
        "toEmail": "",
        "routing": None,
        "fromName": "Manfred Jünemann Mess- und Regeltechnik GmbH",
        "from": "info@juenemann-instruments.de",
        "replyTo": "verkauf@juenemann-instruments.de",
        "bcc": "",
        "subject": "Vielen Dank für Ihre Anfrage!",
        "message": (
            "Guten Tag {Ansprechpartner:7},\r\n\r\n"
            "vielen Dank, dass Sie unser {form_title} genutzt haben. "
            "Wir haben Ihre Anfrage erhalten und bearbeiten diese umgehend. "
            "Ihr Angebot erhalten Sie in der Regel innerhalb von 24h.\r\n\r\n"
            "Falls Sie in der Zwischenzeit weitere Informationen benötigen "
            "oder Fragen haben, können Sie gerne direkt auf diese E-Mail antworten.\r\n\r\n"
            "Wir bedanken und für Ihr Interesse und freuen uns, Ihnen weiterhelfen zu dürfen.\r\n\r\n"
            "Eine Kopie Ihrer Anfrage finden Sie am Ende dieser E-Mail.\r\n\r\n"
            "Mit freundlichen Grüßen\r\n\r\n"
            "Manfred Jünemann Mess- und Regeltechnik GmbH\r\n"
            "Max-Planck-Str. 49\r\n"
            "32107 Bad Salzuflen\r\n"
            "Tel.: 05222 80568 0\r\n"
            "mail: verkauf@juenemann-instruments.de\r\n\r\n"
            "{all_fields}"
        ),
        "disableAutoformat": False,
        "notification_conditional_logic_object": "",
        "notification_conditional_logic": "0",
        "conditionalLogic": None,
        "to": "32",
        "cc": "",
        "enableAttachments": False,
        "isActive": True,
        "toField": "32",
        "advanced_conditional_logic_data": "null",
        "gfacl_prepared_notifications": True
    })

    # Assign the new sections
    form_data["confirmations"] = new_confirmations
    form_data["notifications"] = new_notifications

    # Derive output filename from the "title"
    out_title = form_data["title"].strip()
    output_filename = out_title + ".json"

    # Dump the updated JSON to the new file
    try:
        with open(output_filename, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
        print(f"Output written to: {output_filename}")
    except Exception as e:
        print(f"Error writing updated JSON to '{output_filename}': {e}")


def main():
    parser = argparse.ArgumentParser(description="Process JSON to replace confirmations and notifications.")
    parser.add_argument("-f", "--file", help="Process a single .json file.")
    parser.add_argument("--all", action="store_true", help="Process all .json files in the current directory.")

    args = parser.parse_args()

    # If both are specified or neither, print usage.
    if (args.file and args.all) or (not args.file and not args.all):
        parser.print_help()
        sys.exit(1)

    if args.all:
        # Process all JSON files in the current directory
        for file_name in os.listdir('.'):
            if file_name.lower().endswith('.json'):
                print(f"\nProcessing file: {file_name} ...")
                process_file(file_name)
    else:
        # Process the single specified file
        process_file(args.file)


if __name__ == "__main__":
    main()