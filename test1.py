
"""
inputNum, represents the number of rows and columns of the chess board (N).
"""
def funcChessBoard(inputNum):
	# Write your code here
	board_size = int(inputNum)
	rows = int(inputNum)
	columns = int(inputNum)
	for x in range(inputNum): 
			print("WB")
	for x in range(inputNum):
		print("WB")
	return

def main():
	#input for inputNum
	inputNum = int(input())
	print("hello")
	
	result = funcChessBoard(inputNum)
	print(result)	

if __name__ == "__main__":
	main()