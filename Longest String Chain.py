class Solution:
    def longestStringChain(self, words):
        # Sort words by length
        words.sort(key=len)
        # Dictionary to store the longest chain length for each word
        longest_chain = {}
        max_length = 1
        
        # Iterate through each word
        for word in words:
            longest_chain[word] = 1  # Initial chain length is 1
            # Generate all possible predecessors
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in longest_chain:
                    longest_chain[word] = max(longest_chain[word], longest_chain[predecessor] + 1)
            max_length = max(max_length, longest_chain[word])
        return max_length
