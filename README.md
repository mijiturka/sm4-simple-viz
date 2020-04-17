This project provides some simple visualisations for files produced by
an RHK SM4 microscope.

It depends entirely on  Mirco Panighel's rhksm4 for reading the files:
https://gitlab.com/rhksm4/rhksm4

# Get Mirco's awesome code

Download or `git clone` https://gitlab.com/rhksm4/rhksm4

This is a modified version of the code that works for machines that don't record
RHK_PiezoSensitivity_Tube X and Y: https://gitlab.com/rumyana/rhksm4

# Make our own venv because we're awesome
Make sure we're using python3 - rhksm4 doesn't seem to work with python2

We can use a virtualenv to make a python environment we can mess around with
without affecting our computer's python environments:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

# Install the stuff we need, in this venv only
```
(venv) pip install -r requirements.txt
```

We need to install Mirco's awesome code separately
because it requires numpy,
but pip builds all listed requirements before it installs them.

We're installing this from our local folder,
so if we make any changes to Mirco's code, we need to redo this step
for any changes to take effect.

Assuming we've placed rhksm4 in the top folder,
```
(venv) pip install rhksm4/
```

# Science!

Create some folders:
```
(venv) mkdir inputs outputs
```

Place some SM4 files in the `inputs` folder

Run:
```
(venv) python batch.py
```

to get per-page visual representations in .png format in the `outputs/` folder.
