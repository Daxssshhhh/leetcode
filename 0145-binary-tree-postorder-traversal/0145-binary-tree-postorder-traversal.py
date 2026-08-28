class Solution(object):
    def postorderTraversal(self, root):
        cur, stack = root, []
        visit = []
        result = []

        stack.append(cur)
        visit.append(False)

        while stack:
            cur, v = stack.pop(), visit.pop()

            if cur:
                if v:
                    result.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)

                    stack.append(cur.right)
                    visit.append(False)

                    stack.append(cur.left)
                    visit.append(False)

        return result