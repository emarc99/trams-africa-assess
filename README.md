# trams-africa-assessment

## Algorithm Explanation:
The `fill_filter` function of the algorithm solves the problem of filtering a collection of dictionaries (data structures) based on specified key-value pairs or patterns. Here's a breakdown of how it works:

1. `haystack`: This is a list of dictionaries, where each dictionary represents an individual dataset or record.
2. `needle`: This is a list of strings, where each string represents a key or a subkey (dot-separated for nested dictionaries). The value can be specified, or the wildcard "*" can be used to allow any value for that key.
3. **Main Logic:**
For each dictionary in haystack, it iterates over the list needle.
If a key exists in the current dictionary, it checks the value or subvalue (for nested keys).
The * wildcard allows for a flexible match when any value for a key is acceptable.
4. **Output:**
The function returns a list of dictionaries (result), where each dictionary contains only the key-value pairs (or subkey-value pairs) that match the given patterns in the needle.

## Example:

```python
haystack = [
    {"user": {"name": "Alice", "age": 30}, "location": "NY"},
    {"user": {"name": "Bob", "age": 25}, "location": "LA"},
    {"user": {"name": "Charlie", "age": 35}, "location": "SF"},
]

needle = ["user.name", "location"]

print(fill_filter(haystack, needle))
```
The result would return the names and locations of each user.

## Data Use Cases:
Here are five different relevant data use-cases where this algorithm can be applied:

**1. User Profile Filtering:**
You can use this algorithm to filter user profile data based on specific criteria. For example, given a list of user profiles (dictionaries), you can extract only the relevant details such as name, age, or location.

- **Example:** Filter users based on their country or state and include only users who have a specific role.

**2. Product Data Search:**
In e-commerce, this could be used to filter product catalogs. The `haystack` could be a list of products with various attributes like price, category, and brand. The `needle` would specify which attributes or nested properties you're looking for.

- **Example:** Filter products by brand and show only items under a certain price range.

**3. Event Logs Processing:**
The function could be used to process a list of system event logs or error reports. You can filter out only the relevant error types or events based on specific conditions, making it easier to search through large logs.

- **Example:** Extract logs that match a certain error type or occurred at a certain time.

**4. Sensor Data Analysis:**
In IoT applications, this can help filter sensor readings from different devices. The `haystack` could contain sensor data, and the `needle` could specify which sensors or data ranges to focus on.

- **Example:** Filter temperature sensor readings from different locations, focusing only on abnormal readings.

**5. Survey Results Aggregation:**
For survey data, you can extract relevant responses based on certain questions or demographic information. The `haystack` would contain responses, and the `needle` would specify which questions or demographic fields to extract.

- **Example:** Extract responses only from a certain age group or region.
