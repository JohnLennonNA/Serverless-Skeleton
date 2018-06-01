# Lambda Structure

Simple project to start with lambda and serverless arquiteture

### Prerequisites

   - Docker 
   - NPM
   - Make (Unix)
   
### Installing

        npm install -g serverless
        npm i --save-dev serverless-plugin-simulate
        
  After to install this app's you need to generate the env file, select your service and rename the 
  'env.yml.dist' to 'env.yml'

### Building

  first install the dependences of the function with:

    make lib 'Service/Function'
    
  after execute the command:
  
    make up 'Service/Function'

## Running the tests

TODO!

## Deployment

The deploy is based in Serverless framework, but i maked a simple command to abstract this

To configure credentials: 
    
     serverless config credentials --provider aws --key YOURKEYHERE --secret YOURSECRET
     make deploy Service/Function

and after

     Make deploy 'Service/Function'


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details