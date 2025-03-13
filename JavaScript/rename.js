function renameFields(arrayOfObjects) {
  return arrayOfObjects.map(obj => {
    // Destructuring for clarity
    const { _id, name, ...rest } = obj;

    // Find the array field dynamically
    let arrayFieldKey = Object.keys(rest).find(key => Array.isArray(rest[key]));

    // Build the new object with renamed fields
    return {
      value: _id,
      label: name,
      children: arrayFieldKey ? rest[arrayFieldKey] : undefined,
      ...rest // Preserve any other fields
    };
  });
}
const originalData = [
  { _id: '1', name: 'Item A', someArray: [1, 2, 3] },
  { _id: '2', name: 'Item B', otherArray: ['x', 'y'] }
];

const transformedData = renameFields(originalData);
console.log(transformedData);
