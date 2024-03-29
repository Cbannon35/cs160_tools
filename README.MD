
<h1 id="welcome">Welcome to CS160 Tools</h1>


<p>This repo houses a script used in the <a href="cs160su23.com" target="_blank">Summer 2023 offering of CS 160</a> at UC Berkeley. The script was used to automate email response from staff for students that request excused absences or extensions on assignemnts.</p>

<p>This script can be extended/adapted to other course offerings or purposes, but it is designed to fetch information from Airtable, then use that information to send emails to recipiants, using gmail.</p>

<!-- TABLE OF CONTENTS taken from https://github.com/ma-shamshiri/Pacman-Game/blob/master/README.md?plain=1-->
<h2 id="table-of-contents">Table of Contents</h2>

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


<h2 id="Requirements">Requirements</h2>

<h4>Environment Variables</h4>

Create a `.env` file in the root of the project and then add:

```
AIRTABLE_API_KEY=[your airtable oauth key]
EMAIL_SENDER=[your email here]
```


 
<h4>Email permissions</h4>

You will also need to put a `credentials.json` in the root. This is generated from Google via their Gmail api. I followed <a href="https://mailtrap.io/blog/python-send-email-gmail/#Is-there-an-alternative" target="_blank">this tutorial here</a>.

<h4>Airtable fields</h4>
Lastly, make sure each record you want to fetch from your airtable base has the following fields
<ul>
  <li>Emailed (checkbox) ~ will not be fetched from airtable (assumes already fetched and emailed)</li>
  <li>Approved (checkbox) ~ used to differentiate students in their request status</li>
  <li>Email Text (string) ~ the body of the email</li>
  <li>Wait (checkbox) ~ allows you to prevent selected records from being fetched</li>
</ul>


<h2 id="example-workflow">Example Workflow</h2>
<details>
  <summary>Arguments</summary>
<ul>
    <li><code>[TABLE]</code> ~ specify an airtable base (ex: <code>absence</code> or <code>extension</code>)</li>
    <li><code>[OPTION]</code> ~ either <code>students</code> or <code>emails</code></li>
</ul>
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

