import numpy as np 
import h5py


class feature:
	def hdf5_file_create(self):
		self.f=h5py.File("test.hdf5","w")

	def create_folder(self):
		folder1=input("enter ur folder name")
		self.group1=self.f.create_group(folder1)
	def create_dataset(self):
		self.datasetname=input("enter ur dataset name")
		self.dataset=self.f.create_dataset(self.datasetname,(10,),dtype="i")
		self.data=np.arange(10)
		self.dataset[...]=self.data
		self.f.close()
	def load_dataset(self):
		self.f=h5py.File("test.hdf5","r")
		self.dataset=self.f[self.datasetname]
		self.data = self.dataset[...]
		print (self.data)

obj=feature()
obj.hdf5_file_create()
obj.create_folder()
obj.create_dataset()
obj.load_dataset()
