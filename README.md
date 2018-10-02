# Lunchtime!

---

## Setup

*Please run with python 3 (I used 3.7.0) & the latest version of npm (tested on Chrome and Safari)*

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ npm i
$ npm run build-dev
$ python3 app.py
```

*note, if you don't have npm I've included a prebuilt file so the following steps are sufficient*

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 app.py
```

## Test

```
$ python3 test_lunchtime_matching.py
```

## Approach

- While I'm more experienced with Django, I decided to use Flask for this project as its much more lightweight
  - If authentication/login was needed I would use Django since that's built-in
- For persistance I used python3's shelve utility
  - shelve is part of python3's standard lib and requires no setup
  - shelve is based on python's pickle object serializer
  - while not quite performant at scale, shelve is suitable for the purposes of this project
  - the data is structured as follows:
  ```
  {
    USER_LIST: [...] # persisted list of all users (some preloaded initially)
    <user>: {
      lunch_matches: [...],
      coffee_matches: [...]
    }
  }
  ```
- On the frontend, I used React
  - I followed the smart/dumb component approach, wherein the container components manage the data and perform ajax requests
  - the child components are only concerned with displaying whatever data is fed to them
  - all interaction in the child component is propagated and handled on the parent component via callback props
- Tests were written using pythons built-in unittest lib

## Possible improvements

- Additional unit tests around the matching algorithms would be useful, particularly edge cases
- React component unit tests would also be useful here
- tests against the shelve utility would help determine the point in which it becomes too cumbersome to handle the data
- additional validation against user input (e.g. more anti-xss protection)
- some of the html styles can be improved (the button is mostly unstyled)
- the tests can live in their own folder ideally

