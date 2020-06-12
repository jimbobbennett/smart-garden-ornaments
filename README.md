# Smart Garden Ornaments

*Ever wanted to track things happening in your garden and neighborhood using smart garden ornaments? Now you can using BBC micro:bits and a cloud-based IoT service.*

<!-- TODO - add photo -->

This is a fun week long project for those who want to take their first steps into the world of the Internet of Things (IoT) using devices that are popular with kids and tools that make programming accessible to young developers. You'll use a Raspberry Pi along with some [BBC micro:bits](https://microbit.org) and any garden ornaments you have to hand to build a smart neighborhood, gathering data such as temperature and noise levels and displaying it in the cloud using [Azure IoT Central](https://azure.microsoft.com/services/iot-central/?WT.mc_id=smart_garden_ornaments-github-jabenn).

## How it works

Each smart garden ornament is based around a [BBC micro:bit](https://microbit.org), programmed using [Microsoft MakeCode](https://microbit.org/code/). These micro:bits sit inside whatever ornament you have, such as a bird box or garden gnome, and gather data about the outside world. This data can come from the built-in temperature sensor, or external sensors such as microphones, proximity senors or soil moisture sensors. These micro:bits will then send this data to other micro:bits via the built-in radio. Each micro:bit will forward on the message just like passing notes in class until it reaches a 'hub' micro:bit connected to a Raspberry Pi. This will then send the message on to the cloud to plot on a chart.

<!-- TODO - add photo -->

This project is not limited to one household - if you have neighbors they can also have smart garden ornaments as long as they are positioned close enough for the micro:bits to talk to each other. If you want to share data between households that are further apart, you can do this by using multiple hubs all connected to the same cloud service.

## What you'll need

### The Hub

For the 'hub' that allows your micro:bits to connect to the cloud, you'll need the following:

* A Raspberry Pi running Raspbian or Raspbian Lite. Any Pi will do that has internet connectivity, even the Pi Zero W (but not the base Pi Zero without WiFi).
* An SD card for the Pi, at least 8GB in size
* A BBC micro:bit
* An appropriate USB cable to connect the micro:bit to the Pi. For example if you are using a Pi 3 or 4 you'll need a USB to micro USB cable, if you are using a Pi Zero you'll need a micro USB to micro USB cable or an adapter.
* A USB power supply for the Pi. For the Pi 4 this needs to be USB-C, for other Pis this needs to be micro USB.
* An Azure subscription. Instructions will be provided on how to set this up, and you'll either need to be a student over the age of 18 in higher education to sign up for a student account, or have access to a credit card to sign up for a free account.
  > If you sign up for a free account, your credit card will **NOT** be charged, it is just needed for verification.

<!-- TODO - add photo -->

### Smart garden ornaments

For each smart garden ornament you'll need the following:

* A BBC micro:bit
* A battery pack for the micro:bit
* A garden ornament that can house the micro:bit and keep it dry in the event of rain. This could be a bird box, a garden gnome, fairy house, anything that is outdoor safe and has space to put the micro:bit and battery pack inside.

<!-- TODO - add photo -->

The micro:bits have a temperature sensor built in, so if you are just tracking temperature this is all you'll need. If you want to track other things then you'll need different sensors. Some need to be purchased as a sensor (such as a microphone to track noise levels or a proximity sensor), others such as a soil moisture sensor can be made yourself. This project will cover the following sensors:

<!-- TODO - add sensors -->
* Home made soil moisture sensor

> The cloud service used may come with a small cost. It is free for the first 2 devices used, so if you want to use more smart ornaments they your will be billed. If you have signed up for a student or free account this can come from the credit you are given on sign up leading to no actual cost. The cost at the time of writing is US$0.40 per additional device per month. You can read more details on pricing on the [Azure IoT Central pricing page](https://azure.microsoft.com/pricing/details/iot-central/?WT.mc_id=smart_garden_ornaments-github-jabenn).

## How this guide is structured

This guide is broken down into a number of days. For each day the project should take no more than about an hour and adds another part to the project. Each day will contain multiple parts, labelled as either beginner or advanced. The advanced parts should be done by someone with some experience, the beginner parts are ideal for those just getting started with block based programming. Older kids with some programming experience may be able to complete the entire project, but will require an adult to set up the Azure resources as these may require a credit card and require a sign up from someone over the age of 18.

Follow the links below to access the steps for each day:

* [Day 1 - setup the cloud services](./days/1-setup.md)
* [Day 2 - connect to the cloud](./days/2-connect.md)
* Day 3 - build a mesh network to track temperatures
* Day 4 - build your first smart garden ornament
* Day 5 - add additional sensors
* [Additional ideas](./additional-ideas/)
  * Add multiple hubs so more households can get involved
  * Add rules to get alerts when a sensor value is in a given range

All the code you need for the Pi and micro:bit is all in the [`code`](./code/) folder. Each step will include full instructions on the code you need, including code listings and the micro:bit code both as JavaScript code that can be pasted into MakeCode and pictures of the blocks that you can create yourself.

## Contributing to this project

We'd **LOVE** you to contribute to this project! If you find mistakes in this guide please raise an issue or a PR. If you have additional ideas for ways to extend this project, or want to add instructions for more sensors please fork this repo and add them to the [Additional ideas](./additional-ideas/) section in a PR. We'd also love it if you want to share your stories - how did you set this up, what ornaments did you use, what data did you gather. Please fork the repo raise a PR to add these to the [Stories](./stories/) section. All contributions must follow our code of conduct.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=smart_garden_ornaments-github-jabenn). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=smart_garden_ornaments-github-jabenn) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Learn more, get certified

If you want to learn more about Azure IoT Services, then check out the following:

* [IoT learning paths on Microsoft Learn](https://docs.microsoft.com/learn/browse/?term=IOT&WT.mc_id=smart_garden_ornaments-github-jabenn)
* [The IoT show on Channel9](https://channel9.msdn.com/Shows/Internet-of-Things-Show/?WT.mc_id=smart_garden_ornaments-github-jabenn)

Once you have upskilled as an IoT developer, why not get certified with our upcoming AZ-220 Azure IoT Developer certification. Check out the details on our [certification page](https://docs.microsoft.com/learn/certifications/azure-iot-developer-specialty?WT.mc_id=smart_garden_ornaments-github-jabenn)