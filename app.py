[     UTC     ] Logs for balance-de-materialozano.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[16:11:52] 🖥 Provisioning machine...

[16:11:52] 🎛 Preparing system...

[16:11:52] ⛓ Spinning up manager process...

[16:11:52] 🚀 Starting up repository: 'balance-de-materia1', branch: 'main', main module: 'app.py'

[16:11:52] 🐙 Cloning repository...

[16:11:53] 🐙 Cloning into '/mount/src/balance-de-materia1'...

[16:11:53] 🐙 Cloned repository!

[16:11:53] 🐙 Pulling code changes from Github...

[16:11:53] 📦 Processing dependencies...

Check if streamlit is installed

cat: /mount/admin/install_path: No such file or directory


──────────────────────────────── Installing Streamlit ──────────────────────────────────


Using uv pip install.

Using Python 3.13.6 environment at /home/adminuser/venv

Resolved [2025-09-05 16:11:54.793621] 37 packages[2025-09-05 16:11:54.793987]  in 673ms

Prepared [2025-09-05 16:12:00.180404] 37 packages[2025-09-05 16:12:00.180683]  [2025-09-05 16:12:00.180966] in 5.38s[2025-09-05 16:12:00.181214] 

Installed 37 packages in 413ms

 + altair==5.5.0

 + attrs==25.3.0

 + blinker==1.9.0

 + cachetools==6.2.0

 + certifi==2025.8.3

 + charset-normalizer==3.4.3

 + click==8.2.1

 + gitdb==4.0.12

 + gitpython==3.1.45

 + idna==3.10[2025-09-05 16:12:00.596171] 

 + jinja2==3.1.6

 + jsonschema==4.25.1

 + jsonschema-specifications==2025.4.1

 + markupsafe==3.0.2

 + narwhals==2.3.0

 + numpy==2.3.2

 + packaging==25.0

 [2025-09-05 16:12:00.596414] + pandas==2.3.2

 + pillow==11.3.0

 + protobuf==6.32.0

 + pyarrow==21.0.0

 + pydeck==0.9.1

 + python-dateutil==2.9.0.post0

 + pytz==2025.2[2025-09-05 16:12:00.596571] 

 + referencing==0.36.2

 + requests==2.32.5

 + rpds-py==0.27.1

 + six==1.17.0

 + smmap==5.0.2

 + streamlit[2025-09-05 16:12:00.596790] ==1.49.1

 + tenacity==9.1.2

 + toml==0.10.2

 + tornado==6.5.2

 + typing-extensions==4.15.0

 + tzdata==2025.2[2025-09-05 16:12:00.596967] 

 + urllib3==2.5.0

 + watchdog==6.0.0


────────────────────────────────────────────────────────────────────────────────────────


[16:12:01] 📦 Processed dependencies!

cat: /mount/admin/install_path: No such file or directory




/mount/src/balance-de-materia1/app.py:107: SyntaxWarning: invalid escape sequence '\c'

/mount/src/balance-de-materia1/app.py:106: SyntaxWarning: invalid escape sequence '\c'

  """)

2025-09-05 16:12:13.390 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling

    result = func()

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec

    exec(code, module.__dict__)  # noqa: S102

    ~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/mount/src/balance-de-materia1/app.py", line 103, in <module>

    $M3 = M1 \cdot \frac{{X1 - X2}}{{X3 - X2}} = {m1_input:.2f} \cdot \frac{{({x1_input:.2f} - 1.0)}}{{({x3_input:.2f} - 1.0)}} = {m3_result:.2f} \text{ kg}$

                                                                                                                                                         ^^

NameError: name 'kg' is not defined

[16:12:48] 🐙 Pulling code changes from Github...

[16:12:49] 📦 Processing dependencies...

[16:12:49] 📦 Processed dependencies!

[16:12:50] 🔄 Updated app!

2025-09-05 16:14:39.866 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling

    result = func()

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec

    exec(code, module.__dict__)  # noqa: S102

    ~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/mount/src/balance-de-materia1/app.py", line 103, in <module>

    $M3 = M1 \cdot \frac{{X1 - X2}}{{X3 - X2}} = {m1_input:.2f} \cdot \frac{{({x1_input:.2f} - 1.0)}}{{({x3_input:.2f} - 1.0)}} = {m3_result:.2f} \text{ kg}$

                                                                                                                                                         ^^

NameError: name 'kg' is not defined

2025-09-05 16:14:45.143 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling

    result = func()

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec

    exec(code, module.__dict__)  # noqa: S102

    ~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/mount/src/balance-de-materia1/app.py", line 103, in <module>

    $M3 = M1 \cdot \frac{{X1 - X2}}{{X3 - X2}} = {m1_input:.2f} \cdot \frac{{({x1_input:.2f} - 1.0)}}{{({x3_input:.2f} - 1.0)}} = {m3_result:.2f} \text{ kg}$

                                                                                                                                                         ^^

NameError: name 'kg' is not defined

2025-09-05 16:14:52.476 Uncaught app execution

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling

    result = func()

  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec

    exec(code, module.__dict__)  # noqa: S102

    ~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/mount/src/balance-de-materia1/app.py", line 103, in <module>

    $M3 = M1 \cdot \frac{{X1 - X2}}{{X3 - X2}} = {m1_input:.2f} \cdot \frac{{({x1_input:.2f} - 1.0)}}{{({x3_input:.2f} - 1.0)}} = {m3_result:.2f} \text{ kg}$

                                                                                                                                                         ^^

NameError: name 'kg' is not defined
