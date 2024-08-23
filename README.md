# glottolog-heurist

Script for finding glottolog language id matches for a spreadsheet of
languages from the OMAA Heurist database.

Requires a local, indexed copy of Glottolog and [uv](https://docs.astral.sh/uv/)
for package management

    git clone git@github.com:glottolog/glottolog.git

Then use the pyglottolog tool to build an index (this takes about 15m). Note
that ```uvx``` will download and install pyglottolog in its own venv: 

    cd glottolog
    uvx --from pyglottolog glottolog searchindex

Then use ```uv run``` to run the script

    uv run src/glottolog/glottolog.py