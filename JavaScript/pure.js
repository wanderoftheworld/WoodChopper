/**
 * Splits a string containing Dart parameters, ensuring that parameter declarations within 
 * brackets, quotes, and other scope-defining structures are not split. 
 * 
 * @param parameters The string containing Dart parameters to split.
 * @param separator The pattern used to separate parameters (defaults to commas with optional whitespace).
 * @param limit (Optional) Limits the number of splits.
 * @returns An array of the split parameter strings.
 */
function paramSplit(parameters, separator, limit=50) {
  // Handle edge case: Empty or whitespace input
  if (!parameters || parameters.trim() === "") {
    return [];
  }

  const divider = '*<-$X->*'; // Unique marker for temporary replacement

  // Precalculate bracket and quote positions for efficiency
  const bracketPositions = getMatchingPositions('()', '{}', '[]', '<>', parameters);
  const quotePositions = getMatchingPositions("'", '"', parameters);

  // Combine positions and sort for iteration
  const positions = [...bracketPositions, ...quotePositions]
    .sort((a, b) => a.start - b.start);

  let result = parameters;

  // Iterate through positions and replace with the divider outside of protected areas
  for (let i = 0; i < positions.length; i++) {
    const currentRange = positions[i];
    const previousRange = positions[i - 1] || { start: 0, end: 0 };

    const prefix = parameters.substring(previousRange.end, currentRange.start);
    const middlePart = parameters.substring(currentRange.start, currentRange.end); // Protected part
    const suffix = parameters.substring(currentRange.end); // End may include separator

    // Create a RegExp with the 'global' flag if needed
    let replacementPattern = separator;
    if (separator instanceof RegExp && !separator.global) {
      replacementPattern = new RegExp(separator.source, separator.flags + 'g');
    }

    // Replace separators in the prefix and suffix parts
    result = prefix.replace(replacementPattern, divider) + middlePart + suffix.replace(replacementPattern, divider);
  }

  // Split by the divider and return the result
  return result.split(divider, limit);
}
param1 = 'String user = "John Johnson"'
param2 = 'Map<String, dynamic> json'
console.log(paramSplit(param1))
console.log(paramSplit(param2))
