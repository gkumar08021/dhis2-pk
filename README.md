# dhis2-pocket-knife

Command-line tools to interact with [DHIS2](https://dhis2.org) REST API in bulk.

## Installation

* *pip python package manager* must be installed (check [installation instructions](https://pip.pypa.io/en/stable/installing))
* `pip install dhis2-pocket-knife`

## Usage
* Run `<scriptname>.py --argument1=<something>` and the arguments as required. It should be callable from anywhere, no need to change directories.
* Be sure the specified user has the authorities to run these tasks for the specified DHIS2 server. Test it with `--server=play.dhis2.org/demo --username=admin --password=district`
* It logs to a log file called `dhis2-pocket-knife`

## Bulk sharing settings of objects

**Script name:** `share-objects.py`

Apply sharing settings for DHIS2 objects (dataElements, indicators, programs, ...) based on metadata object filtering. This assumes structured object properties (e.g. all object names / codes have the same prefix or suffix).

| argument  |description   |required?   |
|---|---|---|
|`-s` / `--server`   |server base, e.g. play.dhis2.org/demo   | yes  |
|`-t` / `--object_type`   |type of object, e.g. dataElements   |yes   |
|`-f` / `--filter`   |metadata object filter(s) (case sensitive), e.g. name:like:vaccine - **[docs](https://dhis2.github.io/dhis2-docs/master/en/developer/html/dhis2_developer_manual_full.html#webapi_metadata_object_filter)**   |yes   |
|`-w` / `--usergroup_readwrite`  |name of usergroup which should get Read-Write access   |no   |
|`-r` / `--usergroup_readonly`   |name of usergroup which should get Read-Only access   |no   |
|`-a` / `--publicaccess` | public access (with login), e.g. readwrite, readonly, none   |yes   |
|`-u` / `--username`   |DHIS2 username   |yes   |
|`-p` / `--password`   |DHIS2 password   |yes   |

Example:

`share-objects.py --server=play.dhis2.org/demo --object-type=dataElements --filter="name:like:Vaccine&code:^!like:CORE_DE" --usergroup_readwrite="Bo District Management" --usergroup_readonly="Bo District hospitals" --publicaccess=none --username=admin --password=district`

## Find users with a misconfigured Organisation Unit assignment

**Script name:** `user-orgunits.py`

Returns all users of an Organisation Unit that are configured like below. Users who are assigned both an Orgunit **and** sub-Orgunit can be a source of access errors.
![issue](https://i.imgur.com/MXiALrL.png)

|argument   |description   |
|---|---|
|`-s` / `--server`   |server base, e.g. play.dhis2.org/demo   |
|`-o` / `--orgunit`   |Orgunit UID to check its users     |
|`-u` / `--username`   |DHIS2 username   |
|`-p` / `--password`   |DHIS2 password   |

Example:

`user-orgunits.py --server=play.dhis2.org/demo --orgunit=JdhagCUEMbj --username=admin --password=district`

## Bulk deletion of metadata objects

**Script name:** `delete-objects.py`

Delete metadata objects based on a list of UIDs in a text file. Note: [baosystems/dish2](https://github.com/baosystems/dish2#remove-metadata-objects) may be an alternative.

|argument   |description   |
|---|---|
|`-s` / `--server`   |server base, e.g. play.dhis2.org/demo   |
|`-t` / `--object_type`   |type of metadata object, e.g. dataElements   |
|`-i` / `--uid_file`   |text file with UIDs split by newline/break     |
|`-u` / `--username`   |DHIS2 username   |
|`-p` / `--password`   |DHIS2 password   |

Example:

`delete-objects.py --server=play.dhis2.org/demo --uid_file="UIDs.txt" --username=admin --password=district`

---
PyPI link: https://pypi.python.org/pypi/dhis2-pocket-knife

# Debugging

Request/response debugging: set `debug_flag` in Class src.core.Logger to `True`

## TODO

- share-objects.py: support for multiple userGroup names, support for UIDs