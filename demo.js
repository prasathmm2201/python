// const name = "prasath"
// let str = "prasath welcome";

// // console.log(name.split("").reverse().join())

// let new_name = ""
// for(let i = name.length - 1; i >=0 ; i-- ){
//     new_name += name[i]
// }
// console.log(new_name)


// for(let i = 0; i < name.length; i++){
//     console.log(i)
// }

// console.log(str.replace('welcome' ,'end'))


// function replaceFun(originalStr , target , replacement){
//     let result = ""
//     let i = 0

//     while (i < originalStr.length){
//         if(originalStr.slice(i , i + target.length) === target){
//             result += replacement
//             i += target.length
//         }
//         else{
//             result+= originalStr[i]
//             i++
//         }
//     }

//     return result
// }


// console.log(replaceFun(str ,'welcome' ,'end' ))

const args = process.argv.slice(2);
let jsonFileNames = [];

// Parse the --files argument
args.forEach((arg, index) => {
    console.log(arg)
  if (arg === "--files" && args[index + 1]) {
    jsonFileNames = args[index + 1].split(",");
  }
});
