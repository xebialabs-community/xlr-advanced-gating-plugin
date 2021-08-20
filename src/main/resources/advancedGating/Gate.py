#
# Copyright 2021 Digital.ai
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

if not useOutput and not gatePassed:
    raise Exception("Gate failed with results list: {}".format(results))

table = u"""
|Condition|Result|
|---|---|
"""
for index, condition in enumerate(conditions.keys()):
    result = u"\u2714" if results[index] else u"\u2717"
    table += u"|{}|{}|\n".format(unicode(condition, "utf-8") + u"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", result)
print(table)