#!/bin/bash
# run with `. export_data.sh`
PWD=`pwd`

run () {
	python manage.py dumpdata register_events --output apps/register_events/fixtures/data.json
}

run