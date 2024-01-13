dictionary={"set":"A set is a collection of distinct elements with no specific order. In mathematics and computer science, sets are used to represent a group of objects where each object is unique, and the order of the elements doesn't matter.",
            "matrices":"Matrices are rectangular arrays of numbers, symbols, or expressions arranged in rows and columns. They are commonly used in various fields, including mathematics, physics, computer graphics, and engineering, to represent and manipulate data for purposes like solving systems of linear equations, transforming geometric shapes, and more. Matrices have specific rules for addition, multiplication, and other operations that make them useful in solving a wide range of problems",
            "reflexive":"in the context of a mathematical relation like equality, if a relation R is reflexive, it means that for any element x, R(x, x) holds true, indicating that every element is related to itself.",
            "symmetric":"In mathematics, a symmetric relationship or property means that it is unchanged when you switch the order of its elements. For example, in a symmetric matrix, the elements are the same when reflected across its main diagonal.",
            "transitive":"Transitive is a term used to describe a relation or operation in mathematics, logic, and other fields. A relation or operation is said to be transitive if, for any elements or statements involved, it follows a particular pattern:"}
print("choose one among->'set','matrices','reflexive',symmetric','transitive'")
print("type your choice here->")
s=input()
print(dictionary[s])