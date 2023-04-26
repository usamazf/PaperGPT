# PaperGPT

PaperGPT is an AI powered research assistant to keep track of latest publications given a set of keywords. The system is designed to enable researchers to track latest publications in different conferences, journals, archives etc as well as to summarize matched publications.

## How to use:

### 一、Run with python scripts

This method should work equally fine on Windows, MAC or Ubuntu systems.

Use the following steps to get started:
1. Clone the repository and enter the project directory to your local machine or a server of your choice:
  ```
  git clone https://github.com/usamazf/PaperGPT.git
  cd PaperGPT
  ```

2. Install dependencies:```
pip install -r requirements.txt
```

3. Modify parameters in the `configs/configurations.yaml`. To get more detail on all available parameters refer to docs.

4. Obtain an API key from `OpenAI` and add it to `apikey.ini` if GPT integration is desired. Otherwise turn the GPT module off in `configurations.yaml`.

5. Run PaperGPT.py file:
  ```
  python PaperGPT.py
  ``` 


### 二、Running with Docker

Docker containers are not implemented yet. Feel free to fork and implement then. Issue a pull request once finished implementing.


## Note:

All changes are made on the dev-branch and tested extensively before pulling them into the main branch. Main branch is where you will find the latest stable and working code. Use dev-branch instead if you are looking to explore latest features.


## Issues

Having issues? Just report in [the issue section](https://github.com/usamazf/PaperGPT/issues). **Thanks for the feedback!**


## Contribute

Fork this repository, make your changes and then issue a pull request. If you have new ideas that you do not want to implement, file a feature request.


## Support

Consider becoming a patron (**highly appreciated!**):

[![](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/usamazf)

... Or if you prefer a one-time tip:

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/usamazfr)
