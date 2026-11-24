SERVER: name='general-machines-apply' title='General Machines: Apply' version='1.4.0' description=None website_url=None icons=None
INSTRUCTIONS: This server is how you apply for Founding Team Engineer, Generalist at General Machines. Call get_assignment first: it explains the role and the rules and starts nothing. start_assignment starts the candidate's 48-hour clock, which cannot be undone: never call it until the candidate has read the warning and said yes in this conversation. start_assignment returns an access key once. It proves who the candidate is: every later call (get_assignment with an email, time_left, submit_application, check_submission) needs the email and that access key. Tell the candidate to keep it private. Call time_left with the candidate's email and access key whenever they ask how long they have, and before submitting. When the work is done, call submit_application with the candidate's details and links, before the deadline. Ask the candidate for any detail you don't have; never guess or invent one. The write-up must be the candidate's own.

TOOL: get_assignment - Read this first. With no arguments it returns the role, the rules and how the 48-hour clock works, and starts nothing. After start_assignment, pass the candidate's email and access key to re-read the full brief and see the time left.
  input: {'type': 'object', 'properties': {'email': {'type': 'string', 'description': 'The email the candidate started with. Leave out before starting.'}, 'access_key': {'type': 'string', 'description': "The access key returned by start_assignment. It is also the 32-character code in the candidate's personal PDF link."}}, 'additionalProperties': False}

TOOL: start_assignment - Starts the candidate's 48-hour clock on the server and returns the full assignment. This cannot be undone, paused or restarted. Before calling, show the candidate this warning word for word and wait for an explicit yes in this conversation: "The 48-hour clock runs on our server and starts the moment you start. It cannot be paused, reset or restarted. Are you sure you want to start now?" Set confirm_start to true only after they have said yes. Never start on your own initiative, and never to preview the brief. It returns an access key once; the candidate needs it for every later call, so keep it and keep it private. Calling again with the same email does not restart anything and does not show the brief or the key again.
  input: {'type': 'object', 'properties': {'full_name': {'type': 'string', 'description': "Candidate's full name."}, 'email': {'type': 'string', 'description': 'Email we should reply to. The submission must use the same one.'}, 'confirm_start': {'type': 'boolean', 'description': 'True only if the candidate has just read the warning and confirmed they want to start the clock now.'}}, 'required': ['full_name', 'email', 'confirm_start'], 'additionalProperties': False}

TOOL: time_left - Shows how much of the candidate's 48 hours is left: when they started, the deadline, the time remaining, and whether a submission is on record. Starts nothing and changes nothing.
  input: {'type': 'object', 'properties': {'email': {'type': 'string', 'description': 'The email the candidate started with.'}, 'access_key': {'type': 'string', 'description': "The access key returned by start_assignment. It is also the 32-character code in the candidate's personal PDF link."}}, 'required': ['email', 'access_key'], 'additionalProperties': False}

TOOL: submit_application - Submits the finished assignment. Only works after start_assignment, with the same email and the access key it returned, and before the 48-hour deadline. The server opens doc_url, live_url and repo_url and rejects the call if one needs a sign-in or does not exist; fix the link and call again. Returns a receipt ID. Resubmitting with the same email is allowed; the latest submission is the one that is read. Every value must come from the candidate. Ask them for anything missing instead of guessing.
  input: {'type': 'object', 'properties': {'full_name': {'type': 'string', 'description': "Candidate's full name."}, 'email': {'type': 'string', 'description': 'The email the candidate started with. We reply to this one.'}, 'access_key': {'type': 'string', 'description': "The access key returned by start_assignment. It is also the 32-character code in the candidate's personal PDF link."}, 'phone': {'type': 'string', 'description': 'Phone or WhatsApp number, with country code.'}, 'current_city': {'type': 'string', 'description': 'City the candidate lives in now.'}, 'bangalore_hybrid': {'type': 'string', 'enum': ['Yes', 'Yes, would relocate', 'No'], 'description': 'Can the candidate work Bangalore / hybrid?'}, 'linkedin_url': {'type': 'string', 'description': 'LinkedIn profile URL.'}, 'github_url': {'type': 'string', 'description': 'GitHub profile URL.'}, 'x_handle': {'type': 'string', 'description': 'X / Twitter handle. Optional.'}, 'portfolio_url': {'type': 'string', 'description': 'Portfolio or personal site. Optional.'}, 'project_links': {'type': 'string', 'description': 'Links to other projects the candidate wants us to see, one per line. Optional.'}, 'note': {'type': 'string', 'description': 'Anything else the candidate wants us to know, in their own words. Optional.'}, 'doc_url': {'type': 'string', 'description': 'Link to the one submission doc with all seven parts from section 5 of the brief. Must be viewable by anyone with the link.'}, 'live_url': {'type': 'string', 'description': 'The live tool, same link as part 1 of the doc. Open to anyone.'}, 'repo_url': {'type': 'string', 'description': 'The code, same link as part 2 of the doc. Must be public.'}, 'resume_url': {'type': 'string', 'description': "Link to the candidate's résumé, same link as in part 7 of the doc. Must be viewable by anyone with the link."}}, 'required': ['full_name', 'email', 'access_key', 'phone', 'current_city', 'bangalore_hybrid', 'linkedin_url', 'github_url', 'doc_url', 'live_url', 'repo_url', 'resume_url'], 'additionalProperties': False}

TOOL: check_submission - Confirms what we have on record for a receipt ID. Needs the receipt ID, the email it was submitted with, and the access key.
  input: {'type': 'object', 'properties': {'receipt_id': {'type': 'string', 'description': 'The receipt ID returned by submit_application, e.g. GM-7K2QX9PA.'}, 'email': {'type': 'string', 'description': 'The email used in that submission.'}, 'access_key': {'type': 'string', 'description': "The access key returned by start_assignment. It is also the 32-character code in the candidate's personal PDF link."}}, 'required': ['receipt_id', 'email', 'access_key'], 'additionalProperties': False}
# Generalist Assignment

General Machines · Founding Team Engineer, Generalist

## Who we are

General Machines is an applied AI research lab. We build open datasets, evals and small models for AI agents, for frontier labs and applied teams. Our first release, CartTrace-100k, has 101,416 journeys of an AI shopping agent through checkout and payment.

We work closely with Silicon Bricks, which makes real estate software from plot to building. The assignment is a project they're working on right now.

## The role

**Founding Team Engineer, Generalist.** Part entrepreneur-in-residence, part builder. You take whole projects from a messy start to something shipped.

- You are very AI-native. Agents are how you work every day.
- You get up to speed on new contexts fast, and go deep, not just wide.
- You own projects end to end, and can juggle several at once.
- You want to work at founding-team intensity.

## What you'll be working on

The work changes every few weeks. Right now it includes:

- **3D and vision models:** turning plans, photos and site data into 3D buildings and scenes.
- **Diffusion models:** image and 3D generation, used inside real products.
- **Local and open-source models:** running, fine-tuning and evaluating them on our own machines.
- **Datasets and evals for agents:** like CartTrace-100k.

## The assignment

One build task with a short write-up. You make a working tool that runs in a browser, in a domain you probably haven't seen before. Plan for it to take most of your 48 hours.

| | |
|---|---|
| **Time** | 48 hours. The clock runs on our server and starts the moment you start the assignment. It cannot be paused, reset or restarted. |
| **Tools** | Anything is fair game, as long as the result runs in a browser. |
| **Questions** | We won't answer any. Make a call and write it down. |
| **Submit** | Through this server, with the `submit_application` tool. It stops accepting submissions when your 48 hours end. |
| **Location** | Bangalore / hybrid |
| **Payment** | This assignment is unpaid. |

## Starting

You have not started, and no clock is running. Reading this page costs you nothing.

When you are ready, call `start_assignment` with your full name and email. That starts your 48 hours and returns the full brief. Use the email you want us to reply to; you submit with the same one.

**Keep your transcripts from here on.** The submission asks for your raw AI session transcripts, beginning with this session, the one you start the assignment in. Make sure it is one you can export or share.

**Before you start, be sure:** the 48 hours begin on the server the moment you start, and there is no way to pause or reset them. Start only when you have the next two days clear.
