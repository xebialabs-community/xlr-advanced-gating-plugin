#
# Copyright 2025 Digital.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

results = [eval(conditions[condition]) for condition in conditions.keys()]
if conditionsType == "AND":
    gatePassed = all(results)
else:
    gatePassed = any(results)

# Print dedicated success or failure message
if gatePassed:
    print("Gate passed successfully!")
else:
    failed_count = len([r for r in results if not r])
    if failed_count == 1:
        print("Gate failed! 1 condition was not satisfied.")
    else:
        print("Gate failed! {} conditions were not satisfied.".format(failed_count))

table = u"""
|Condition|Result|
|:------|:------:|
"""
for index, condition in enumerate(conditions.keys()):
    result = u"\u2714" if results[index] else u"\u2717"
    # Handle both Python 2 and 3 compatibility for unicode
    try:
        condition_text = unicode(condition, "utf-8")
    except NameError:
        # Python 3 - unicode is str
        condition_text = str(condition)
    table += u"|{}|{}|\n".format(condition_text + u"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", result)
print(table)
print("&nbsp;")

if not useOutput and not gatePassed:
    raise Exception("Gate failed")
