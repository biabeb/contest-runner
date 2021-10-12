# No Statement
## Description
It's up to you to figure this problem out.

## Statement
<p>This problem has no description. You must figure out how the input generates the output and write the solution yourself.</p>
<p>Enter your own custom input into the box below, then press 'Test' to run it!</p>

<textarea style="width: 100%" id="textarea" rows="20">
5
31
8
32
128
36
</textarea><br />
<button class="button" style="width: 100%; margin: 0 !important;" id="test">Test</button>
<pre id="pre">
62
16
64
256
72
</pre>

<script>
  var textarea = document.getElementById('textarea');
  var pre = document.getElementById('pre');
  var test = document.getElementById('test');

  function runTest() {
    pre.innerHTML = '';
    fetch('https://e4j7ts2fzd.execute-api.us-east-1.amazonaws.com/Prod/train-car/', {
        method: 'POST',
        body: textarea.value
    }).then(resp => resp.text()).then(text => pre.innerHTML = text);
  }
  test.addEventListener('click', runTest);
</script>

## Input
Unknown

## Output
Unknown

## Constraints
Unknown