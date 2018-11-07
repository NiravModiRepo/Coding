/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };


 LeetCode: https://leetcode.com/problems/validate-binary-search-tree/description/
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {

        if (root == NULL){
            return true;
        }

        return isValidBST(root, (long long int)INT_MIN-1, (long long int)INT_MAX+1);

    }

    bool isValidBST(TreeNode* node, long long int min, long long int max){

        if (node == NULL){
            return true;
        }

        if ((node->val >= max) || (node->val <= min)){
            return false;
        }

        return isValidBST(node->left, min, node->val) && isValidBST(node->right, node->val, max);
    }
};
