# Turtle Card 200X3D

[![My youtube video](https://img.youtube.com/vi/VwDLsoGanac/0.jpg)](https://www.youtube.com/watch?v=VwDLsoGanac)

You can find the instructions to simulate it down below

![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/7d223076-7fa4-43d6-85ef-f7e17b179188)


Before you try it out, I recommend watching my youtube video first if you have no idea what you're doing



# How to run the Graphics Card
1. Make sure you have Logisim Evolution installed.
2. Open 16bitGPU3.circ using Logisim.
3. Select the "multicore" circuit.

![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/0971fff5-8c2d-441f-a178-86df638ed8e3)

4. Go to the "Simulate" tab and make sure Auto-Tick is enabled, and is set to 2048.0 KHz.
<img width="396" alt="image" src="https://github.com/TheCodingTurtle/tortlecard/assets/67763250/c388c14c-196e-4da7-b14f-10a6e27c1ff8">

5. Go from the Design to the Simulate tab on the left and Enable Clock Ticks
<img width="163" alt="image" src="https://github.com/TheCodingTurtle/tortlecard/assets/67763250/046f25f0-6627-4cf8-8115-53aeeb0a6e1a">

6. Press the "RST" button to reset the graphics card and press "1" to start rendering.
<img width="700" alt="image" src="https://github.com/TheCodingTurtle/tortlecard/assets/67763250/98808e99-02aa-47b1-81b1-1a9934391094">

Optional: You can use these two DIP switches to set the position of the light source in binary.
![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/b94c8973-2cfe-4e87-b789-69f4887a3b05)

# How to change the object it renders

1. Open pointplotter.py and replace the output file location to your preferred location. (make sure it is a .hex file)
![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/1bbd463a-0e7e-41cf-9139-6115a8b48ebb)

2. Select which of the template shapes you want to render by uncommenting them or create your own.
![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/68bcd846-76d6-447a-90be-5ae19d275178)
![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/2e34c42a-d803-4620-8131-b48ef7d65903)

3. Run the program.

4. Open the turtle card in Logisim Evolution, and make sure to import the output hex files A, B, and types into the corresponding ROMs.
![image](https://github.com/TheCodingTurtle/tortlecard/assets/67763250/e6ab98d7-e0da-4424-9baa-ce61ea5f7e62)

5. Follow the "How to run the Graphics Card" instructions

(if you are stuck and don't know what to do in any of these steps, make sure to rewatch my youtube video or leave a comment with your problem)


