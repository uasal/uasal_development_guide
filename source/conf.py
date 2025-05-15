# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'uasal_development_guide'
copyright = '2025, UASAL'
author = 'UASAL'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
html_static_path = []
html_theme_options = {
    'vcs_pageview_mode': 'blob', # 'blob' shows the file view, 'edit' shows the edit view
    # 'display_github': True, # Deprecated in newer versions, use vcs_pageview_mode
}
    
_source_suffix = locals().get('source_suffix', '.rst') # Get source_suffix if defined

# --- SETTINGS FOR REPO LINK ---

# GitHub username or organization name
github_user = "uasal"
# Repository name
github_repo = "uasal_development_guide"
# Default branch name (CHECK THIS on GitHub: usually 'main' or 'master')
github_version = "main"
# Path in the repository root where your documentation lives
# (Relative path from repo root to the directory containing conf.py)
# CHECK THIS: Use '/docs/' if conf.py is in a 'docs' folder at the root
# Use '/' if conf.py is directly in the repository root.
conf_py_path = "/source/"

html_context = {
    # Enable "Edit on GitHub" link:
    'display_github': True,
    # Provide GitHub details:
    'github_user': github_user,
    'github_repo': github_repo,
    'github_version': github_version,
    'conf_py_path': conf_py_path,
    # Set the source file suffix (for edit links)
    'source_suffix': _source_suffix,
}

linkcheck_request_headers = {
    r'https://www.datacamp.com/': {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; '
                                                'rv:24.0) Gecko/20100101 Firefox/24.0'}
}

# Parameters for the linking and link checking

linkcheck_allowed_redirects = {
# All HTTP redirections from the source URI to
# the canonical URI will be treated as "working".
    r'https://Duck.ai': r'https://duckduckgo.com*',
    r'http://10.130.30.9/*': r'http://10.130.30.9/users/sign_in',
    r'https://github.com/settings/*':r'https://github.com/login*'
    r'https://github.com/git-lfs/git-lfs#installing*': r'https://github.com/git-lfs/git-lfs?tab=readme-ov-file#installing'
}


# Ignore links that are private repos or require VPN
linkcheck_ignore = [
   'http://10.130.30.9/*',
   'https://github.com/uasal/spacecoron_design_docs/*',
   'https://github.com/uasal/wcc_designdocs/*',
   'https://gitlab.sc.ascendingnode.tech*',
   'https://github.com/uasal/lab_documents*',
   'https://github.com/uasal/uasal_archive'
]

# Sites where the anchoring doesn't work correctly (often a redirect issue)
# linkcheck_anchors_ignore_for_url = ['https://github.com/git-lfs/git-lfs*']