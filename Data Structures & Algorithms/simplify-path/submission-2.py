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
        result = ""
        while stack:
            result = "/" + stack.pop() + result
        return result if result else "/"
                


        