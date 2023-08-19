def getFTEScore(org, scores, emp_id):
  # returns a hashmap from emp_id to their scores
  if emp_id not in scores:
    score = 1.0
    for c in org[emp_id]:
      score += getFTEScore(org, scores, c)
    scores[emp_id] = score
  return scores[emp_id]

# return emp_id of CEO; None on validation error
def validateOrgChart(org):
  bottomUp = {}
  # Only one root; non-root node has single parent.
  for k in org.keys():
    for c in org[k]:
      if c in bottomUp:
        print('Found node w/ more than 1 parents', c)
        return None
      bottomUp[c] = k

  ceo_id = None
  for k in org.keys():
    if k not in bottomUp:
      if ceo_id:
        print('Found more than 1 top players', ceo_id, k)
        return None
      ceo_id = k

  if ceo_id:
    if not hasCycle(ceo_id, []):
      return ceo_id
    print('Found cycle')
  return None

# return True if a cycle is detected
def hasCycle(id, visited):
  for c in org[id]:
    if c in visited:
      print('Cycle!')
      return True 
    if hasCycle(c, visited + [c]):
      return True
  return False

org = {"123": ["234", "345"],
   "234": ["456", "789"],
   "345":[],
   "456":[],
   "789":['123']}
#scores = {}
#getFTEScore(org, scores, '123')
#print(scores)
ceo_id = validateOrgChart(org)
if ceo_id:
  print('CEO is', validateOrgChart(org))
