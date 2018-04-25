import re


print """
<style>
  li.paper {
  }
  p.session {
    margin-top: 1em;
  }
  span.time {
    width: 15ex;
    text-align: left;
  }
  span.authors {
    display: block;
    font-size: smaller;
  }
  span.title {
    display: block;
    font-weight: bold;
  }
  span.toggle {
    font-size: 10pt;
    display: block;
    cursor: pointer;
  }
  span.toggle:hover {
    text-decoration: underline;
  }
  span.abstract {
  }
</style>
"""


print """
 <section class='row'>
   <div class="col-full">"""

with file("./tmp") as f:
  pid = None
  firstsession = False
  for l in f:
    if not l.strip(): 
      print ""
      continue

    if l[0] in "1234567890":
      if firstsession:
        print "</ul>"
      firstsession = True
      time = l.split(" ")[0]
      rest = " ".join(l.split(" ")[1:]).strip()
      print """
      <p class='session'>
        <span class='time'>%s</span>
        <span class='sessiontitle'>%s</span>
      </p>""" % (time, rest)
      print "<ul>"
    if l[0] == "[":
      pid = int(l.split()[0][1:-1])
      l = " ".join(l.split()[1:])
      authors = l.split(".")[0]
      title = ".".join(l.split(".")[1: ])

      print """
      <li class='paper'>
        <span class='title'>%s</span>
        <span class='authors'>%s</span>
        <span id='toggle_%s' class='toggle'>(toggle abstract)</span>
        <script>
        $(function() {
          $("#toggle_%s").click(function() {
            $("#abstract_%s").toggle()
          });
        })
        </script>
      """ % ( title, authors, pid, pid, pid)
    if l.startswith("Abstract"):
      abstract = l[len("Abstract. "):]
      print """
        <span style='display:none' class='abstract' id="abstract_%s">%s</span>
      </li>
      """ % (pid, abstract)

print """
    </div>
  </section>"""
