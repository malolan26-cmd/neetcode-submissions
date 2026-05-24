/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode tracker  = new ListNode();
        ListNode mergeSortedList = tracker;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                mergeSortedList.next = list1;
                list1 = list1.next;
            } else {
                mergeSortedList.next = list2;
                list2 = list2.next;
            }
            mergeSortedList = mergeSortedList.next;
        }

        if (list1 != null) {
            mergeSortedList.next = list1;
        } else {
            mergeSortedList.next = list2;
        }

        return tracker.next;
        
    }
}