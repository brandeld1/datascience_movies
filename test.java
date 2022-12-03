import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class test {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, DoubleWritable>{

    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      itr.nextToken();
      while(itr.hasMoreTokens()) {
	    	  String data[] = itr.nextToken().toString().split(",");
	    	  if(data.length>=5) {
		          String genresList = data[2];
		          String[] genres = genresList.toString().split("\\|");

		          //DoubleWritable sentiment = new DoubleWritable(Double.parseDouble(data[4])); this is for gathering the sentiment

		          DoubleWritable one = new DoubleWritable(1);
		          //word.set(genres[0]);
		          for(int i=0;i<genres.length;i++){
		        	  String yeargenre = data[1]+","+genres[i];
		        	  word.set(yeargenre);
		        	  context.write(word, one);
		          }
	    	  }
	    }
    }
  }

  public static class DoubleSumReducer
       extends Reducer<Text,DoubleWritable,Text,DoubleWritable> {
    private DoubleWritable result = new DoubleWritable();

    public void reduce(Text key, Iterable<DoubleWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      double sum = 0;
      //int total = 0;
      for (DoubleWritable val : values) {
        sum += val.get();
        //total += 1;
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(test.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(DoubleSumReducer.class);
    job.setReducerClass(DoubleSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(DoubleWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}