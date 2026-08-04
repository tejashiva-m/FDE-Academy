# Day 12 API Examples

## Setup

Use the existing `day11` virtual environment, because it already has `requests` installed.

From `week02/day12`:

```bash
cd /Users/tejashivamekapothula/Documents/FDE-Academy/week02/day12
../day11/.venv/bin/python3 status_codes.py
```

If you want to activate the venv first:

```bash
cd /Users/tejashivamekapothula/Documents/FDE-Academy/week02/day11
source .venv/bin/activate
cd ../day12
python status_codes.py
```

## Run examples

```bash
../day11/.venv/bin/python3 get_request.py
../day11/.venv/bin/python3 post_request.py
../day11/.venv/bin/python3/put_request.py
../day11/.venv/bin/python3 delete_request.py
../day11/.venv/bin/python3 patch_request.py
../day11/.venv/bin/python3 query_parameters.py
../day11/.venv/bin/python3 status_codes.py
```

## What each file does

- `get_request.py`: reads a single post from JSONPlaceholder.
- `post_request.py`: creates a new post.
- `put_request.py`: replaces a post.
- `delete_request.py`: deletes a post.
- `patch_request.py`: updates part of a post.
- `query_parameters.py`: gets posts filtered by query parameters.
- `status_codes.py`: shows an HTTP response status code for a nonexistent post.
