# Complex-Parameters
## How can parameter values be changed within a function?
* Any value can be passed as an argument
* Re-assigning a parameter variable has no effect on the original argument
* Changing information inside the original argument does change it permanently
* This is true even though the variable name ("reference") inside the function is different than the one in the Main Program
* When something about the program changes after a function is run, this is called a "side effect"
## What types of values can be changed?
* Any value that has information inside it can be changed in a function
* For instance:
  * Lists (change the values at indexes)
  * Sprites (change attributes like .image)
  * Rects (change .x and .y locations)
 ## How can a parameter be made optional?
 * Parameters can be made optional by assigning them a default value in the function header
 * Syntax: function_name(parameter=value)
 * There can be as many default parameters as necessary
 * When providing arguments, they will fill in the parameters from left to right
 ## Why are default parameters useful?
 * Some functions are commonly called with the same argument most of the time
 * For example, the value 1 for line width or the value 0 for shape line width
 * By giving these parameters a default, the programmer doesn't have to type them if they're the usual value
 * Flag parameters are often set this way
 ## What other functions can be used on lists?
 * random.choice(list)
   * Takes a list argument
   * Returns a random item from the list
 * random.shuffle(list)
   * Takes a list argument
   * Puts the list in a random order (side effect)
 * list.index(value)
   * Called on a list variable
   * Takes any value as an argument
   * Returns an index for the first time the value appears in the list
   * Causes an error if the item is not in the list
