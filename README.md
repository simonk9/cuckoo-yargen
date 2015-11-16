# cuckoo-yargen
Addon that utilize yarGen to auto-generate yara rule from given sample

About:
=======

this is a quick and dirty poc to use yarGen with Cuckoo to auto-generate yara rules from given sample.
currently this generates a rule for the submited sample, without opcodes, i didnt make it work with the dropped files.

Installation:
=================

1) git clone https://github.com/Neo23x0/yarGen.git

2) cat conf-extra/auxiliary.conf >> conf/auxiliary.conf

or manually add to your aux... the following lines:

[yaragen]
enabled = yes

(this probably shouldnt be aux module, but it works)

3) copy yaragen.py to cuckoo/modules/auxiliary

4) change the paths in yaragen.py to your enviroment (/data/cuckoo/... )

5) add the following line to /web/web/urls.py (i'm quite sure this doesnt work as it should)

url(r"^yara/(?P<task_id>\w+)/(?P<md5>([a-fA-F\d]{32}))/$", "analysis.views.filereport"),

6) add the following to /web/templates/analysis/reports/index.html (in a perfect scenario the if statement should contain "config.yaragen" but i didnt do it)

      {% if config.jsondump %}
        <tr>
          <th>Yara Rules</th>
            <td style="text-align: right;"><a class="btn btn-primary btn-small" href="{% url "analysis.views.filereport" analysis.info.id "yara" %}">Download</a></td>
        </tr>
      {% endif %}

7) add the following line under the function "def filereport(request, task_id, category):" in the file /web/analysis/views.py

        "yara": "report.yara",

=====================

now after you submit a sample it will run yarGen simultaniusly with the cuckoo analysis.
the end result is is a report.yara file under the reports folder in the storage location.
the file can be downloaded from the reports tab in the web intreface if you followed steps 5-7