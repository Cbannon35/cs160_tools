
<h2 id="welcome">Welcome to CS160 Tools</h2>

---

<p>This Repo Houses a script used in the <a href="cs160su23.com" target="_blank">Summer 2023 offering of CS 160</a> at UC Berkeley. The script was used to automate email response from staff for students that request extensions on assignemnts and excused absences.</p>

<p>This script can be extended/adapted to other course offerings or purposes, but it is designed to fetch information from Airtable, then use that information to send emails to recipiants, using gmail</p>

<!-- TABLE OF CONTENTS taken from https://github.com/ma-shamshiri/Pacman-Game/blob/master/README.md?plain=1-->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#welcome"> ➤ About</a></li>
    <li><a href="#setup"> ➤ Setup</a></li>
    <li><a href="#requirements"> ➤ Requirements</a></li>
    <li><a href="#example-workflow"> ➤ Example Workflow</a></li>
   <li><a href="#next-steps"> ➤ Next Steps</a></li>
  </ol>
</details>

<h2 id="setup">Getting Started</h2>
<p>First, clone the repo</p>

```
git clone git@github.com:Cbannon35/cs160_tools.git
```

<p>Run the script</p>

```
cd cs160_tools
python script.py
```

<p>That's it! However, we need a few more things to setup email and airtable permissions...</p>

---

<h2 id="Requirements">Requirements</h2>

<ul>
  <li>
    <details open="open">
    <summary>Environment Variables</summary>
      Create a `.env` file in the root of the project and then add:


      ```
      AIRTABLE_API_KEY=[your airtable oauth key]
      EMAIL_SENDER=[your email here]
      ```


    </details>
  </li>
  <li>
    <details open="open">
    <summary>Email permissions</summary>
      You will also need to put a `credentials.json` in the root. This is generated from Google via their Gmail api. I followed <a href="https://mailtrap.io/blog/python-send-email-gmail/#Is-there-an-alternative" target="_blank">this tutorial here</a>.
    </details>
  </li>
  <li>
  <details open="open">
  <summary>Airtable fields</summary>
    Lastly, make sure each record you want to fetch from your airtable base has the following fields
    <ul>
      <li>Emailed (checkbox) ~ will not be fetched from airtable (assumes already fetched and emailed)</li>
      <li>Approved (checkbox) ~ used to differentiate students in their request status</li>
      <li>Email Text (string) ~ the body of the email</li>
      <li>Wait (checkbox) ~ allows you to prevent selected records from being fetched</li>
    </ul>
  </details>
  </li>
</ul>

---

<h2 id="example-workflow">Example Workflow</h2>
<details>
  <summary>Arguments</summary>
    - `[TABLE]` ~ specify an airtable base (ex: `absence` or `extension`)</li>
    - `[OPTION]` ~ either `students` or `emails`</li>
</details>

<p>Startup the script</p>

```
python3 script.py
```

<p>Fetch from airtable and write approved & rejected students to json</p>

```
fetch [TABLE]
```

<p>Generate emails for students</p>

```
generate
```

<p>Email students</p>

```
email
```

Note: You can view records you fetched or emails you generate `view [OPTION]`
Note: You can also clear fetched records or generated emails `clear [OPTION]`

---

<h2 id="next-steps">Next Steps</h2>
<ul>
  <li>Move content from bases_and_tables.py to .env?
  <details>
    Not too worried about privacy because of Airtable's permissions sytstem. Also makes more sense if people are working on the same base
  </details>
  </li>
  <li>Make script more robust
  <details>
  Because this script had an end goal in mind it was incredibly simple to just whip it up in python. But, this means the line was blurred between how much logic should reside in airtable, and how much should reside locally. Airtable also provides great scripting tools, so potentially, there will be less logic to work with in python as it will be delegated to airtable (e.g moved subject and cc fields to airtable from `email_template.json`)
  </details>
  </li>
<li>Cleanup Naming to make script more readable</li>
<ul>

