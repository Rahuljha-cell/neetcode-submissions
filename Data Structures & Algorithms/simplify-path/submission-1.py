class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split("/"):
            if token == "" or token == ".":
                continue
            if token != "..":
                stack.append(token)
            elif stack:
                stack.pop()
        return "/" + "/".join(stack)
                


        