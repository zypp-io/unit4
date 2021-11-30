<p align="center">
  <img alt="logo" src="https://www.zypp.io/static/assets/img/logos/zypp/white/500px.png"  width="200"/>
</p>

# Template repository for packages
Template repository for Zypp projects which eventually will be released as a package. 
This can be used as an initial template when creating a project on GitHub. 
Not all folders have to be used when not needed, for example `data` or `docs` can be specific per project.

### How to use this template
 1. When creating a new project on GitHub, you can choose a template project.
 2. When you cloned the repository, adjust the `setup.cfg` with your own information of the project. Things like name, urls, keywords, author etc.
 3. Replace the name of the project in `.github/workflows/ci.yaml`.   
 4. Remove the folders you don't need.
 5. Optional: rename the `src` folder to the project name.

### Scripts
This template contains two utility scripts:
1. `check_setupcfg_and_requirementst_equal.py` which checks if the requirements in `setup.cfg` and `requirements.txt` are equal. Setup.cfg is leading, but in many cases you want a requirements.txt for testing locally.
2. `generate_requirements_from_setup.py` can be used to create a new `requirements.txt` from `setup.cfg` to prevent manually copying and pasting.
