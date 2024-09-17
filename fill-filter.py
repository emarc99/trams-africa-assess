def fill_filter(haystack, needle):
    result = []

    for stack in haystack:
        new_result = {}
        for pin in needle:
            if "." in pin:
                key, value = pin.split(".", 1)
            else:
                key, value = pin, stack.get(pin)

            if key in stack and (value != "*" or value is None):
                spook = stack[key]
                if value is None or value in spook:
                    new_result.setdefault(key, {})[value] = spook.get(value)
            elif key in stack and value == "*":
                spook = stack[key]
                new_result[key] = list(spook.values()) if isinstance(spook, dict) else None

        result.append(new_result)

    return result
