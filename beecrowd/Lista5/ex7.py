def predict_robot_position(test_cases):
    for _ in range(test_cases):
        num_instructions = int(input())
        instructions = []
        position = 0

        for _ in range(num_instructions):
            instruction = input().strip()

            if instruction.startswith("SAME AS"):
                i = int(instruction.split()[2])
                instruction = instructions[i-1]

            if instruction == "LEFT":
                position -= 1
            elif instruction == "RIGHT":
                position += 1

            instructions.append(instruction)

        print(position)

test_cases = int(input())
predict_robot_position(test_cases)