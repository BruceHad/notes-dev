## Factory Pattern
# Design Patters

https://addyosmani.com/resources/essentialjsdesignpatterns/book/

## Factory Pattern

The Factory petter is about creating objects. A Factory can provide an interface for creating objects, where we can specify the type of factory object we wish to be created.

Imagine a UI factory where we are asked to create a type of UI component. Rather than creating the component directly using the new operator or something, we ask the Factory for a component. It creates the object and returns it to us.

This is useful if the creation process is complex. 

    function Car( options ){
        this.door = options.doors || 4;
        this.state = options.state || "new";
        this.color = options.color || "brown";
    }
    
    function Truck( options){
      this.state = options.state || "used";
      this.wheelSize = options.wheelSize || "large";
      this.color = options.color || "blue";
    }
    
    function VehicleFactory(){ }
    
    // Default vehicleClass is "car".
    VehicleFactory.prototype.vehicleClass = Car;
    VehicleFactory.prototype.createVehicle = function( options ){
        switch(options.vehicleType){
            case "car":
                this.vehicleClass = Car;
                break;
            case "truck":
                this.vehicleClass = Truck;
                break;
        }
        return new this.vehicleClass( options );
    }
    var carFactory = new VehicleFactory();
    
    var car = carFactory.createVehicle({
        vehicleType: "car",
        color: "yellow",
        doors: 6
    });
    
The factory pattern can be useful when:

* The object or component set up is complex.
* When we need to easily generate different instances of objects.
* When we're working with many small objects or components that share the same properties.

Done use when: applied to the wrong type of problem (???). 
