from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant specialized in software engineering."},
        {"role": "user", "content": """I am looking at a github package called deepdespeckling, here is the structure of the package : 
├── LICENSE
├── MANIFEST.in
├── Makefile
├── README.md
├── build
│   ├── bdist.macosx-10.9-universal2
│   └── lib
│       └── deepdespeckling
│           ├── __init__.py
│           ├── denoiser.py
│           ├── despeckling.py
│           ├── merlin
│           │   ├── __init__.py
│           │   ├── inference
│           │   │   ├── __init__.py
│           │   │   └── merlin_denoiser.py
│           │   ├── merlin_denoiser.py
│           │   ├── saved_model
│           │   │   ├── spotlight.pth
│           │   │   └── stripmap.pth
│           │   └── training
│           │       ├── Dataset.py
│           │       ├── GenerateDataset.py
│           │       ├── __init__.py
│           │       ├── model.py
│           │       ├── saved_model
│           │       │   └── model.pth
│           │       └── train.py
│           ├── model.py
│           ├── sar2sar
│           │   ├── __init__.py
│           │   ├── sar2sar_denoiser.py
│           │   └── saved_model
│           │       └── sar2sar.pth
│           ├── test_deepdespeckling.py
│           └── utils
│               ├── __init__.py
│               ├── constants.py
│               ├── load_cosar.py
│               └── utils.py
├── deepdespeckling
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── denoiser.cpython-39.pyc
│   │   ├── despeckling.cpython-39.pyc
│   │   └── model.cpython-39.pyc
│   ├── denoiser.py
│   ├── despeckling.py
│   ├── merlin
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   └── merlin_denoiser.cpython-39.pyc
│   │   ├── merlin_denoiser.py
│   │   └── saved_model
│   │       ├── spotlight.pth
│   │       └── stripmap.pth
│   ├── model.py
│   ├── sar2sar
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   └── sar2sar_denoiser.cpython-39.pyc
│   │   ├── sar2sar_denoiser.py
│   │   └── saved_model
│   │       └── sar2sar.pth
│   ├── test_deepdespeckling.py
│   └── utils
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-39.pyc
│       │   ├── constants.cpython-39.pyc
│       │   ├── load_cosar.cpython-39.pyc
│       │   └── utils.cpython-39.pyc
│       ├── constants.py
│       ├── load_cosar.py
│       └── utils.py
├── deepdespeckling.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── not-zip-safe
│   ├── requires.txt
│   └── top_level.txt
├── dist
│   ├── deepdespeckling-0.2.0-py3-none-any.whl
│   ├── deepdespeckling-0.2.0.tar.gz
│   ├── deepdespeckling-0.2.1-py3-none-any.whl
│   ├── deepdespeckling-0.2.1.tar.gz
│   ├── deepdespeckling-0.2.2-py3-none-any.whl
│   ├── deepdespeckling-0.2.2.tar.gz
│   ├── deepdespeckling-0.2.3-py3-none-any.whl
│   ├── deepdespeckling-0.2.3.1-py3-none-any.whl
│   ├── deepdespeckling-0.2.3.1.tar.gz
│   ├── deepdespeckling-0.2.3.tar.gz
│   ├── deepdespeckling-0.2.4-py3-none-any.whl
│   ├── deepdespeckling-0.2.4.tar.gz
│   ├── deepdespeckling-0.2.5-py3-none-any.whl
│   ├── deepdespeckling-0.2.5.tar.gz
│   ├── deepdespeckling-0.2.6-py3-none-any.whl
│   ├── deepdespeckling-0.2.6.tar.gz
│   ├── deepdespeckling-0.2.7-py3-none-any.whl
│   ├── deepdespeckling-0.2.7.tar.gz
│   ├── deepdespeckling-0.2.8-py3-none-any.whl
│   └── deepdespeckling-0.2.8.tar.gz
├── icons
│   ├── build.svg
│   ├── doc.svg
│   └── pypi.svg
├── img
│   ├── coordinates
│   │   ├── denoised_test_image_data.png
│   │   ├── noisy_test_image_data.png
│   │   └── processed_image
│   ├── crop
│   │   ├── arrow_down.png
│   │   ├── crop_example.png
│   │   ├── denoised_test_image_data.png
│   │   └── noisy_test_image_data.png
│   └── entire
│       ├── denoised.png
│       ├── merlin_tests
│       │   └── IMAGE_HH_SRA_spot_068.cos
│       ├── noisy.png
│       ├── sar2sar_denoised.png
│       ├── sar2sar_noisy.png
│       └── sar2sar_tests
│           └── s1a-iw-grd-vv-20190508t055909-20190508t055934-027132-030ee6-001.tiff
├── setup.py
└── tox.ini

33 directories, 100 files

Can you suggest another folders and files structure by keeping the same tree format ? """},
    ]
)
# Print the generated response
print(response.choices[0].message.content)
