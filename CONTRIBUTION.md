## Build and push to pypi
- Create virtual env:
```
git checkout https://github.com/connext-biz/zalo_integration.git
cd zalo_integration
virtualenv .
pip install -r requirements.txt
. bin/activate
```

- Install `twine`:
```
pip install twine
```

- Bump package version: change version in `setup.py` file, commit and push to Github.

- Run build command:
```
python3 -m build --wheel `pwd`
```

- Push to pypi. You need to have an account on [pypi.org](https://pypi.org/) first.
```
twine upload dist/zalo_sdk-<new-version>-py3-none-any.whl
```
