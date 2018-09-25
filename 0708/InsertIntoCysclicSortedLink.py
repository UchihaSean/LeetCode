class Solution(object):
	def insert(self, head, insertVal):
		"""
		:type head: Node
		:type insertVal: int
		:rtype: Node
		"""

		new_node = Node(insertVal, None)
		if not head:
			new_node.next = new_node
			return new_node

		cur = head

		while not (cur.val < insertVal <= cur.next.val):

			# cur is max, and cur.next is min. If max < v or min >= v, we stop
			if cur.next.val <= cur.val:
				if cur.val < insertVal or cur.next.val >= insertVal:
					break

			cur = cur.next

		new_node.next, cur.next = cur.next, new_node
		return head