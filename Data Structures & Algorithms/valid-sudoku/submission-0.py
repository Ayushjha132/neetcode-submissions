from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        # rows
        # for i in range(9):
        #     check_dict = {}
        #     for j in range(9):
        #         current_item = board[i][j]
        #         if current_item == ".":
        #             continue
        #         if current_item in check_dict:
        #             return False
        #         check_dict[current_item] = True

        # # cols - just change the row instead of col
        # for j in range(9):   
        #     check_dict = {}
        #     for i in range(9):
        #         current_item = board[i][j]
        #         if current_item == ".":
        #             continue
        #         if current_item in check_dict:
        #             return False
        #         check_dict[current_item] = True
        
        # # square check
        # for sr in range(0, 9, 3):
        #     for sc in range(0, 9, 3):
        #         check_dict = {}
        #         # check in a square
        #         for i in range(3):
        #             for j in range(3):
        #                 current_item = board[i+sr][j+sc]
        #                 if current_item == ".":
        #                     continue
        #                 if current_item in check_dict:
        #                     return False
        #                 check_dict[current_item] = True
        # return True

    # Optimal method 
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_item = board[r][c]
                if current_item == ".":
                    continue
                if (current_item in rows[r] or 
                    current_item in cols[c] or 
                    current_item in squares[(r // 3, c // 3)]):
                    return False   

                rows[r].add(current_item)
                cols[c].add(current_item)
                squares[(r // 3, c // 3)].add(current_item)

        return True